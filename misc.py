from typing import Optional
import unrealsdk


def isClient() -> bool:
    """Returns true if the current netmode is configured as client."""
    return int(unrealsdk.GetEngine().GetCurrentWorldInfo().NetMode) == 3


def checkClassName(
    obj: unrealsdk.UObject, expectedClass: str, expectedName: Optional[str] = None
) -> bool:
    if obj is None:
        raise RuntimeError(f"object of class {expectedClass} must not be none")

    if obj.Class is None:
        raise RuntimeError(f"object is not a class, but expected class {expectedClass}")

    foundClass = obj.Class.GetName()
    if foundClass != expectedClass:
        raise RuntimeError(
            f"expected object of class {expectedClass} but got {foundClass}"
        )

    if expectedName:
        foundName = obj.GetObjectName()
        if foundName != expectedName:
            raise RuntimeError(
                f"expected object with path {expectedName} but got {foundName}"
            )
