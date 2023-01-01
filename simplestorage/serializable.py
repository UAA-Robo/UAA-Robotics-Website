from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime

class Serializable(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def to_json_str(self):
        pass

    @abstractmethod
    def from_dict(self):
        pass

@dataclass
class Person(Serializable):
    id: str
    user: bool
    viewer: bool
    admin: bool
    first_name: str
    last_name: str
    username: str
    email: str
    phone: str

    create_date: datetime
    date_of_birth: datetime
    last_modified_date: datetime

    notes: str

    role_history: dict  # are we really going to need this?

    # ethnographic and optional data
    major: str = "N/A"
    ethnicity: str = "N/A"
    gender: str = "N/A"
    discord_handle: str = None
    github_username: str = None

@dataclass
class Ticket(Serializable):
    id: str
    created_by: str
    ticket_number: int
    assigned_to: list[Person]

