from io_files.dataclass import ProblemData, SolutionData


def user_has_not_provided_arguments(args):
    return len(args) <= 2

def read_file(filename: str) -> ProblemData:
    file_content = open(filename, 'r').read()
    lines = file_content.split("\n")
    line_1 = lines[0].split(" ")
    line_2 = [ int(el) for el in lines[1].split(" ")]
    
    return ProblemData(
        max_slices=int(line_1[0]),
        number_of_types=int(line_1[1]),
        types=line_2,
    )

def write_submission(data: SolutionData) -> str:
    return f"{data.number_of_types}\n{' '.join(data.types)}"