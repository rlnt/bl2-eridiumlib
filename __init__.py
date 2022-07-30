# pyright: reportMissingModuleSource=false
import unrealsdk
import sys
import webbrowser
from typing import Any, Dict, Optional, cast

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

import asyncio
import socket
import ssl

import requests  # noqa: E402
import semver  # noqa: E402

__all__ = [
    "log",
    "isClient",
    "getCurrentPlayerController",
    "getCurrentWorldInfo",
    "getCurrentGameInfo",
    "getSkillManager",
    "getActionSkill",
    "getVaultHunterClassName",
    "checkLibraryVersion",
    "checkModVersion",
    "EridiumMod",
    "keys",
    "debug",
    # redistributed modules
    "requests",
    "semver",
    "socket",
    "ssl",
    "asyncio",
]
__version__ = "0.4.2"


def log(mod: SDKMod, *args: Any) -> None:
    unrealsdk.Log(f"[{mod.Name}]", *args)


def isClient() -> bool:
    """Returns true if the current netmode is configured as client."""
    return int(unrealsdk.GetEngine().GetCurrentWorldInfo().NetMode) == 3


def getCurrentPlayerController() -> unrealsdk.UObject:
    """Returns the local player."""
    return cast(unrealsdk.UObject, unrealsdk.GetEngine().GamePlayers[0].Actor)


def getCurrentWorldInfo() -> unrealsdk.UObject:
    """Returns the current world info."""
    return cast(unrealsdk.UObject, unrealsdk.GetEngine().GetCurrentWorldInfo())


def getCurrentGameInfo() -> unrealsdk.UObject:
    """Returns the current game info."""
    return cast(unrealsdk.UObject, getCurrentWorldInfo().Game)


def getSkillManager() -> unrealsdk.UObject:
    """Returns the global skill manager from the game info."""
    return cast(unrealsdk.UObject, getCurrentGameInfo().GetSkillManager())


def getActionSkill(PC: Optional[unrealsdk.UObject] = None) -> unrealsdk.UObject:
    """Returns the action skill of a player controller.

    A player controller can be passed in.
    If no player controller is passed in, the local player will be used.
    """
    if PC is None:
        PC = getCurrentPlayerController()

    return cast(unrealsdk.UObject, PC.PlayerSkillTree.GetActionSkill())


def getVaultHunterClassName(PC: Optional[unrealsdk.UObject] = None) -> str:
    """Returns the class name of a Vault Hunter of a player controller.

    A player controller can be passed in.
    If no player controller is passed in, the local player will be used.
    """
    if PC is None:
        PC = getCurrentPlayerController()

    return str(PC.PlayerClass.CharacterNameId.CharacterClassId.ClassName)


def validateVersion(version: str) -> str:
    if version[0] == "v":
        version = version[1:]
    return version


def getLatestVersion(repository: str) -> str:
    """
    Gets the latest public release tag name of a passed in repository.
    Will raise an exception if the releases couldn't be fetched.
    """
    try:
        response = requests.get(f"https://api.github.com/repos/{repository}/releases", timeout=30)
        response.raise_for_status()
        releases = response.json()
    except Exception:
        raise

    if len(releases) < 1:
        raise RuntimeWarning(f"{repository} has no releases!")

    return str(releases[0]["tag_name"])


def isLatestRelease(latestVersion: str, currentVersion: str) -> bool:
    """
    Returns True if the current version is equal
    or higher than the latest version.
    """
    return int(semver.compare(validateVersion(currentVersion), validateVersion(latestVersion))) >= 0


def checkModVersion(mod: SDKMod, repository: str) -> None:
    """
    Checks if the mod version is up-to-date.
    Will log the results to the console.
    """
    log(mod, f"Version: v{mod.Version}")

    try:
        latestVersion: str = getLatestVersion(repository)
    except Exception:
        log(mod, "Latest version couldn't be fetched! Skipping version check.")
        return

    if isLatestRelease(validateVersion(latestVersion), validateVersion(mod.Version)):
        log(mod, "Mod is up-to-date!")
    else:
        log(mod, f"Newer version available: {latestVersion}")


def checkLibraryVersion(requiredVersion: str) -> bool:
    """
    Returns True if the version of EridiumLib is compatible.
    If not, opens a page which informs that the EridiumLib version is incompatible.
    """
    import webbrowser

    if int(semver.compare(__version__, validateVersion(requiredVersion))) >= 0:
        return True

    webbrowser.open(
        "https://github.com/DAmNRelentless/bl2-eridiumlib/blob/main/docs/TROUBLESHOOTING.md"
    )
    return False


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
    }

    def __init__(self) -> None:
        self.Status = "Enabled"
        checkModVersion(self, "DAmNRelentless/bl2-eridiumlib")
        log(self, f"Python Version: {sys.version}")
        log(self, f"__debug__: {__debug__}")

    def SettingsInputPressed(self, action: str) -> None:
        if action == "GitHub":
            webbrowser.open("https://github.com/DAmNRelentless/bl2-eridiumlib")
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
