import unrealsdk
from typing import Dict
import webbrowser
from Mods.ModMenu import (
    SDKMod,
    Mods,
    ModTypes,
    EnabledSaveType,
    RegisterMod,
)
from Mods.Eridium import keys, debug
from Mods.Eridium.keys import KeyBinds

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
    players = unrealsdk.GetEngine().GamePlayers
    if len(players) < 1:
        raise RuntimeError("No game players found")

    return players[0].Actor


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

    def Enabled(self):
        log(self, f"Version: {self.Version}")
        log(self, f"__debug__: {__debug__}")

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
