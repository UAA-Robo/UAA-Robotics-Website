"""
Placeholder python script for the time being.

This will contain all the methods that we use to serialize and de-serialize objects into and out of the
database

"""
from abc import ABC, abstractmethod
from os import path
from serializable import Serializable
import json

class DatabaseConnection(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def save_object_by_id(self, obj: Serializable, identifier: str) -> None:
        pass

    @abstractmethod
    def get_object_by_id(self, obj:Serializable, identifier:str) -> Serializable:
        pass


class SimpleObjectStorage(DatabaseConnection):
    """
    SimpleObjectStorage just saves objects as json objects as files, dirt simple, not searchable, not very
    efficient, and you can't run queries on it without iterating through a lot of objects... but we can use this
    as a simple skeleton to design our back end, then as long as we keep this open to open to extension by making any
    other connections we want to use an ABC of the DatabaseConnection I think we'd be all good.
    """
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def save_object_by_id(self, obj: Serializable, identifier: str) -> None:
        with open(path.join(self.folder_path, identifier)) as obj_file:
            json.dump(obj.to_json_str(), obj_file)

    def get_object_by_id(self, obj:Serializable, identifier: str) -> Serializable:
        with open(path.join(self.folder_path, identifier)) as obj_file:
            obj = json.load(obj_file)
            return obj.from_dict()
