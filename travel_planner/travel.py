"""
Main script to show testable functions

Application for planning trips

Author: L. Bleicher
Last modified: 30.09.24

"""

from typing import List


class Travelplan:
    def __init__(self) -> None:
        self.destinations: List[str] = []
        self.max_size = 5

    def add(self, destination: str):
        if self.size() >= self.max_size:
            raise OverflowError("Cannot add more countries.")
        if destination in self.destinations:
            raise ValueError(f"{destination} is already in the travel plan.")
        else:
            self.destinations.append(destination)

    def remove(self, destination: str):
        if destination not in self.destinations:
            raise ValueError(f"{destination} is not in the travel plan.")
        else:
            self.destinations.remove(destination)

    def get_reiseziele(self) -> List[str]:
        return self.destinations

    def size(self) -> int:
        return len(self.destinations)
