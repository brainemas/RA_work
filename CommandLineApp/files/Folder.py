from dataclasses import dataclass
from datetime import datetime


@dataclass
class Folder:
    name: str
    d: datetime
    author: str
