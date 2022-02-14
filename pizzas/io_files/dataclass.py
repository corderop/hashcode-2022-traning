from dataclasses import dataclass
from typing import List


@dataclass
class ProblemData:
    max_slices: int
    number_of_types: int
    types: List[int]
    
@dataclass
class SolutionData:
    number_of_types: int
    types: List[int]