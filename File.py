from dataclasses import dataclass
from datetime import datetime
import Folder


@dataclass
class File:
    name: str
    size: int
    d: str
    author: str
    parent: str
