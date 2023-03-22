"""
    A Staff is owned by a Score, it has a clef which will be applied to the first measure, and a
    list of measures that will be the first in the score. If the first measure's clef value is specified,
    it will replace the Staff's clef value in the score.
"""

from voice import Voice

class Staff:
    def __init__(self, clef="G", measures: list[Voice]=[[]]) -> None:
        self.__defclef = clef
        # measures is a 2d list, each inner list is a measure that contains somewhere from 1 to 4 voices
        self.measures = measures