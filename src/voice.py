"""
    Voices are held in a 2d list called "measures" inside of Staff.
"""
from chord import Chord

class Voice:
    def __init__(self,  chords: Chord=[]) -> None:
        self.chords = chords
