import unrealsdk
import Mods.ModMenu
from Mods.ModMenu import (
    SDKMod,
    Mods,
    ModTypes,
    EnabledSaveType,
    RegisterMod,
)
from Mods.Eridium import missions, keys, misc

__all__ = ["log", "EridiumMod", "missions", "keys", "misc"]


def log(mod: SDKMod, message: str) -> None:
    unrealsdk.Log(f"[{mod.Name}] {message}")


class EridiumMod(SDKMod):
    Name = "Eridium"
    Author = "Chronophylos"
    Description = "A library with common functionality of all our mods"
    Version = "0.1.0"

    Types = ModTypes.Library
    SaveEnabledState = EnabledSaveType.LoadWithSettings
    IsEnabled = True

    def __init__(self):
        log(self, f"Version: {self.Version}")
        log(self, f"__debug__: {__debug__}")


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
