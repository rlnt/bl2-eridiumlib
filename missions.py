import enum
from typing import Iterable, Optional, cast
import unrealsdk
from Mods.Eridium.misc import checkClassName, isClient
from Mods.ModMenu import NetworkManager, ServerMethod
import json


__all__ = [
    "MissionStatus",
    "MissionDefinition",
    "Mission",
    "MissionTracker",
]


class MissionStatus(enum.IntEnum):
    NotStarted = 0
    Active = 1
    RequiredObjectivesComplete = 2
    ReadyToTurnIn = 3
    Complete = 4
    Failed = 5
    MAX = 6

    def canBeActivated(self) -> bool:
        """Returns true if the status is either ReadyToTurnIn or Active."""
        return self in [
            MissionStatus.ReadyToTurnIn,
            MissionStatus.Active,
        ]


class MissionDefinition:
    """A wrapper for a WillowGame.MissionDefinition object."""

    def __init__(self, inner: unrealsdk.UObject):
        checkClassName(inner, "MissionDefinition")

        self._inner: unrealsdk.UObject = inner

    def inner(self) -> unrealsdk.UObject:
        return self._inner

    @property
    def MissionNumber(self) -> int:
        """The id of the mission."""
        return int(self.inner().MissionNumber)

    @MissionNumber.setter
    def MissionNumber(self, number: int) -> None:
        self.inner().MissionNumber = number


class Mission:
    """A wrapper for a WillowGame.IMission.MissionData object."""

    def __init__(self, inner: unrealsdk.FStruct):
        # checkClassName(inner, "IMission.MissionData") # is struct can do :(
        assert inner is not None

        self._inner: unrealsdk.FStruct = inner

    def __repr__(self) -> str:
        return f"IMission.MissionData {self.inner().__repr__()}"

    def inner(self) -> unrealsdk.FStruct:
        return self._inner

    @property
    def MissionDef(self) -> MissionDefinition:
        """The definition of the mission."""
        return MissionDefinition(self.inner().MissionDef)

    @MissionDef.setter
    def MissionDef(self, missionDef: MissionDefinition) -> None:
        self.inner().MissionDef = missionDef.inner()

    @property
    def Status(self) -> MissionStatus:
        """The status of the mission."""
        return MissionStatus(self.inner().Status)

    @Status.setter
    def Status(self, status: MissionStatus) -> None:
        self.inner().Status = status


class MissionTracker:
    """A wrapper for a WillowGame.MissionTracker object."""

    def __init__(self):
        self._inner: unrealsdk.UObject = (
            unrealsdk.GetEngine().GetCurrentWorldInfo().GRI.MissionTracker
        )
        checkClassName(
            self._inner,
            "MissionTracker",
            "Loader.TheWorld.PersistentLevel.MissionTracker",
        )

    def inner(self) -> unrealsdk.UObject:
        return self._inner

    def getMissionByNumber(self, number: int) -> Mission:
        """Returns the mission with the MissionNumber equal to number.

        Raises an IndexError if the mission was not found.
        """
        for mission in self.MissionList:
            if mission.MissionDef.MissionNumber == number:
                return mission
        raise IndexError(f"There is no active mission with the mission number {number}")

    @property
    def MissionList(self) -> Iterable[Mission]:
        """A list of all available missions."""
        return [Mission(m) for m in self.inner().MissionList]

    @MissionList.setter
    def MissionList(self, missionList: Iterable[Mission]) -> None:
        self.inner().MissionList = [
            m.inner() for m in missionList if isinstance(m, Mission)
        ]

    # AttributeError: 'NoneType' object has no attribute 'MissionList'
    # At:
    #   D:\SteamLibrary\steamapps\common\Borderlands 2\Binaries\Win32\Mods\Eridium\missions.py(117): MissionList
    #   D:\SteamLibrary\steamapps\common\Borderlands 2\Binaries\Win32\Mods\Eridium\missions.py(131): getActiveMissions
    def getActiveMissions(self) -> Iterable[Mission]:
        """Returns all active missions sorted by their MissionNumber.

        For a definition of active see `MissionStatus.isActive`-
        """
        activeMissions = sorted(
            [m for m in self.MissionList if m.Status.canBeActivated()],
            key=lambda m: m.MissionDef.MissionNumber,
        )
        return activeMissions

    @property
    def ActiveMission(self) -> MissionDefinition:
        """The currently tracked mission."""
        return MissionDefinition(self.inner().ActiveMission)

    @ActiveMission.setter
    def ActiveMission(self, mission: MissionDefinition) -> None:
        self.setActiveMission(mission)

    def setActiveMission(self, mission: MissionDefinition) -> None:
        """Set the currently tracked mission to mission."""
        if isClient():
            self._serverSetActiveMission(mission.MissionNumber)
        else:
            self._setActiveMission(mission.MissionNumber)

    @ServerMethod
    def _serverSetActiveMission(
        self, number: int, PC: Optional[unrealsdk.UObject] = None
    ) -> None:
        self._setActiveMission(number, PC)

    def _setActiveMission(
        self, number: int, PC: Optional[unrealsdk.UObject] = None
    ) -> None:
        mission = self.getMissionByNumber(number)
        missionDef = mission.MissionDef.inner()
        unrealsdk.Log(missionDef)
        self.inner().SetActiveMission(missionDef, True, PC)

    @staticmethod
    def NetworkSerialize(arguments: NetworkManager.NetworkArgsDict) -> str:
        """
        Called when instances of this class invoke methods decorated with `@ModMenu.ServerMethod`
        or `@ModMenu.ClientMethod`, performing the serialization of any arguments passed to said
        methods. The default implementation uses `json.dumps()`.

        Arguments:
            arguments:
                The arguments that need to be serialized. The top-level object passed will be a
                `dict` keyed with `str`, containing a `list` as well as another `dict`.
        Returns:
            The arguments serialized into a text string.
        """
        return json.dumps(arguments)

    @staticmethod
    def NetworkDeserialize(serialized: str) -> NetworkManager.NetworkArgsDict:
        """
        Called when instances of this class receive requests for methods decorated with
        `@ModMenu.ServerMethod` or `@ModMenu.ClientMethod`, performing the deserialization of any
        arguments passed to said methods. The default implementation uses `json.loads()`.

        Arguments:
            serialized:
                The string containing the serialized arguments as returned by 'NetworkSerialize'.
        Returns:
            The deserialized arguments in the same format as they were passed to `NetworkSerialize`.
        """
        return cast(NetworkManager.NetworkArgsDict, json.loads(serialized))
