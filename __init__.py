# pyright: reportMissingModuleSource=false
import unrealsdk
import sys
import webbrowser
from typing import Any, Dict, cast

from Mods.EridiumLib import debug, keys
from Mods.EridiumLib.keys import KeyBinds

from Mods.ModMenu import EnabledSaveType, ModPriorities, Mods, ModTypes, RegisterMod, SDKMod

if __name__ == "__main__":
    import importlib

    importlib.reload(sys.modules["Mods.EridiumLib.debug"])
    importlib.reload(sys.modules["Mods.EridiumLib.keys"])

    # See https://github.com/bl-sdk/PythonSDK/issues/68
    try:
        raise NotImplementedError
    except NotImplementedError:
        __file__ = sys.exc_info()[-1].tb_frame.f_code.co_filename  # type: ignore

# isort: skip

import site

site.addsitedir("Mods/EridiumLib/dist")

# isort: skip

import socket
import ssl

import requests  # noqa: E402
import semver  # noqa: E402
import ujson  # noqo: E402

__all__ = [
    "log",
    "isClient",
    "getCurrentPlayerController",
    "EridiumMod",
    "missions",
    "keys",
    "debug",
    # redistributed modules
    "requests",
    "semver",
    "ujson",
    # python c modules
    "socket",
    "ssl",
]
__version__ = "0.3.2"


def log(mod: SDKMod, *args: Any) -> None:
    unrealsdk.Log(f"[{mod.Name}]", *args)


def isClient() -> bool:
    """Returns true if the current netmode is configured as client."""
    return int(unrealsdk.GetEngine().GetCurrentWorldInfo().NetMode) == 3


def getCurrentPlayerController() -> unrealsdk.UObject:
    """Returns the local player."""
    return cast(unrealsdk.UObject, unrealsdk.GetEngine().GamePlayers[0].Actor)


def getLatestVersion(repo: str) -> str:
    response = requests.get(f"https://api.github.com/repos/{repo}/releases")
    response.raise_for_status()
    releases = response.json()
    if len(releases) < 1:
        raise RuntimeWarning(f"{repo} has no releases")
    return str(releases[0]["tag_name"])


def isLatestRelease(latest_version: str, current_version: str) -> bool:
    if latest_version[0] == "v":
        latest_version = latest_version[1:]
    if current_version[0] == "v":
        current_version = current_version[1:]

    return int(semver.compare(current_version, latest_version)) >= 0


class EridiumLib(SDKMod):
    Name = "EridiumLib"
    Author = "Chronophylos, Relentless"
    Description = "A library with common functionality of all our mods"
    Version = __version__

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
        try:
            log(self, f"Latest release tag: {getLatestVersion('RLNT/bl2_eridium')}")
        except RuntimeWarning as ex:
            log(self, f"Warning: {ex}")
        log(self, f"Python Version: {sys.version}")
        log(self, f"__debug__: {__debug__}")

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
