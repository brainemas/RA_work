from dataclasses import dataclass


@dataclass
class File:
    name: str
    size: int
    d: str
    author: str
    parent: str
