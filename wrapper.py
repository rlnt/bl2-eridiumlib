from typing import cast
from Mods.ModMenu import NetworkManager
from abc import ABC
import pickle as serializer


class NetworkingClass(ABC):
    @staticmethod
    def NetworkSerialize(arguments: NetworkManager.NetworkArgsDict) -> str:
        """
        Called when instances of this class invoke methods decorated with `@ModMenu.ServerMethod`
        or `@ModMenu.ClientMethod`, performing the serialization of any arguments passed to said
        methods. The default implementation uses `pickel.dumps()`.

        Arguments:
            arguments:
                The arguments that need to be serialized. The top-level object passed will be a
                `dict` keyed with `str`, containing a `list` as well as another `dict`.
        Returns:
            The arguments serialized into a text string.
        """
        return serializer.dumps(arguments)

    @staticmethod
    def NetworkDeserialize(serialized: str) -> NetworkManager.NetworkArgsDict:
        """
        Called when instances of this class receive requests for methods decorated with
        `@ModMenu.ServerMethod` or `@ModMenu.ClientMethod`, performing the deserialization of any
        arguments passed to said methods. The default implementation uses `pickle.loads()`.

        Arguments:
            serialized:
                The string containing the serialized arguments as returned by 'NetworkSerialize'.
        Returns:
            The deserialized arguments in the same format as they were passed to `NetworkSerialize`.
        """
        return cast(NetworkManager.NetworkArgsDict, serializer.loads(serialized))
