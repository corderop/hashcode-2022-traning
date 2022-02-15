from io_files.dataclass import ProblemData, SolutionData


def process_data(data: ProblemData, type: str) -> SolutionData:
    if type == "greedy":
        return greedy(data)

def greedy(data: ProblemData) -> SolutionData:
    solution = []
    current_slices = 0
    
    # O(n)
    for pizza, slices in reversed(list(enumerate(data.types))):
        solution_slices = current_slices + slices
        
        if solution_slices <= data.max_slices:
            solution.append(pizza)
            current_slices += slices

            if solution_slices == data.max_slices:
                break

    # O(n) (reverse)
    solution.reverse()
    
    return SolutionData(
        number_of_types=len(solution),
        types=solution,
    )
            
    
