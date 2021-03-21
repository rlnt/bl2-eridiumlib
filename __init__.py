# pyright: reportMissingImports=false
import unrealsdk
import webbrowser
from typing import Dict

from Mods.Eridium import debug, keys
from Mods.Eridium.keys import KeyBinds

from Mods.ModMenu import EnabledSaveType, ModPriorities, Mods, ModTypes, RegisterMod, SDKMod

if __name__ == "__main__":
    import importlib
    import sys

    importlib.reload(sys.modules["Mods.Eridium.debug"])
    importlib.reload(sys.modules["Mods.Eridium.keys"])

    # See https://github.com/bl-sdk/PythonSDK/issues/68
    try:
        raise NotImplementedError
    except NotImplementedError:
        __file__ = sys.exc_info()[-1].tb_frame.f_code.co_filename  # type: ignore

import site

site.addsitedir("Mods/Eridium/dist")


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
    return str(releases[0]["tag_name"])


def isLatestRelease(latest_version: str, current_version: str) -> bool:
    return int(semver.compare(current_version, latest_version)) >= 0


class EridiumLib(SDKMod):
    Name = "EridiumLib"
    Author = "Chronophylos"
    Description = "A library with common functionality of all our mods"
    Version = "0.2.0"

    Types = ModTypes.Library
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    Priority = ModPriorities.Library

    SettingsInputs: Dict[str, str] = {
        KeyBinds.G.value: "GitHub",
        KeyBinds.D.value: "Discord",
    }

    def __init__(self) -> None:
        self.Status = "Enabled"

        log(self, f"Version: {self.Version}")
        log(self, f"__debug__: {__debug__}")
        try:
            log(self, f"Latest release tag: {getLatestVersion('RLNT/bl2_eridium')}")
        except RuntimeWarning as ex:
            log(self, f"Warning: {ex}")

    def SettingsInputPressed(self, action: str) -> None:
        if action == "GitHub":
            webbrowser.open("https://github.com/RLNT/bl2_eridium")
        elif action == "Discord":
            webbrowser.open("https://discord.com/invite/Q3qxws6")
        else:
            super().SettingsInputPressed(action)


instance = EridiumLib()
if __name__ == "__main__":
    for mod in Mods:
        if mod.Name == instance.Name:
            Mods.remove(mod)
            Mods.append(instance)
            break
RegisterMod(instance)
