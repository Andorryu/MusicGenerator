"""
    A chord has a durationType and notes. If no notes are specified, then it is considered a rest.
"""
from enum import Enum, auto
from note import Note

class Duration(Enum):
    MEASURE = auto
    HALF = auto
    QUARTER = auto
    EIGHTH = auto
    _16TH = auto
    _32nd = auto

class Chord:
    def __init__(self, durationType=Duration.MEASURE, notes: list[Note]=[]) -> None:
        self.durationType = durationType
        self.notes = notes