from dataclasses import dataclass
from typing import List



@dataclass
class Ride:
    idx: int 
    start: List[int]
    finish: List[int]
    earliest_start: int
    latest_finish: int
    
    def __lt__(self, other):
        return self.earliest_start < other.earliest_start

@dataclass
class ProblemData:
    rows: int
    columns: int
    vehicles: int
    number_of_rides: int
    bonus: int
    steps: int
    rides: List[Ride]    

@dataclass
class Vehicle:
    position: List[int]
    step: int
    rides: List[int]

@dataclass
class SolutionData:
    points: int 
    vehicles: List[Vehicle]
    