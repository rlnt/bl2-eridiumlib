import unrealsdk
from typing import Dict
import webbrowser
import importlib
from Mods.ModMenu import (
    SDKMod,
    Mods,
    ModTypes,
    EnabledSaveType,
    RegisterMod,
)
from Mods.Eridium import keys, debug
from Mods.Eridium.keys import KeyBinds

if __name__ == "__main__":
    import sys

    importlib.reload(sys.modules["Mods.Eridium.keys"])

    # See https://github.com/bl-sdk/PythonSDK/issues/68
    try:
        raise NotImplementedError
    except NotImplementedError:
        __file__ = sys.exc_info()[-1].tb_frame.f_code.co_filename  # type: ignore

import site

site.addsitedir("Mods/Eridium/vendor")

# import bundled packages
import requests  # noqa: E402
import semver  # noqa: E402

__all__ = [
    "log",
    "isClient",
    "getCurrentPlayerController",
    "EridiumMod",
    "missions",
    "keys",
    "debug",
]


def log(mod: SDKMod, message: str) -> None:
    unrealsdk.Log(f"[{mod.Name}] {message}")


def isClient() -> bool:
    """Returns true if the current netmode is configured as client."""
    return int(unrealsdk.GetEngine().GetCurrentWorldInfo().NetMode) == 3


def getCurrentPlayerController() -> unrealsdk.UObject:
    """Returns the current player.
    This seems to always be the local player
    """
    return unrealsdk.GetEngine().GamePlayers[0].Actor


def getLatestVersion(repo: str) -> str:
    response = requests.get(f"https://api.github.com/repos/{repo}/releases")
    response.raise_for_status()
    releases = response.json()
    if len(releases) < 1:
        raise RuntimeWarning(f"{repo} has no releases")
    return releases[0]["tag_name"]


def isLatestRelease(latest_version: str, current_version: str) -> bool:
    latest = semver.VersionInfo.parse(latest_version)
    current = semver.VersionInfo.parse(current_version)
    return semver.compare(current, latest) >= 0


class EridiumMod(SDKMod):
    Name = "Eridium"
    Author = "Chronophylos"
    Description = "A library with common functionality of all our mods"
    Version = "0.1.0"

    Types = ModTypes.Library
    SaveEnabledState = EnabledSaveType.LoadWithSettings

    SettingsInputs: Dict[str, str] = {
        KeyBinds.Enter: "Enable",
        KeyBinds.G: "GitHub",
        KeyBinds.D: "Discord",
    }

    def __init__(self):
        log(self, f"Version: {self.Version}")
        log(self, f"__debug__: {__debug__}")
        try:
            log(self, f"Latest release tag: {getLatestVersion('RLNT/bl2_eridium')}")
        except RuntimeWarning as ex:
            log(self, f"Error: {ex}")

    def SettingsInputPressed(self, action: str) -> None:
        if action == "GitHub":
            webbrowser.open("https://github.com/RLNT/bl2_eridium")
        elif action == "Discord":
            webbrowser.open("https://discord.com/invite/Q3qxws6")
        else:
            super().SettingsInputPressed(action)


instance = EridiumMod()
if __name__ == "__main__":
    log(instance, "Manually loaded")
    for mod in Mods:
        if mod.Name == instance.Name:
            if mod.IsEnabled:
                mod.Disable()
            Mods.remove(mod)
            log(instance, "Removed last instance")

            # Fixes inspect.getfile()
            instance.__class__.__module__ = mod.__class__.__module__
            break
RegisterMod(instance)
