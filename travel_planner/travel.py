"""
Main script to show testable functions

Application for planning fitness programs

Author: L. Bleicher
Last modified: 30.09.24

"""

from typing import List


class Travelplan:
    def __init__(self) -> None:
        self.destinations: List[str] = []

    def add(self, destination: str):
        self.destinations.append(destination)

    def get_reiseziele(self) -> List[str]:
        return self.destinations

    def size(self) -> int:
        return len(self.destinations)