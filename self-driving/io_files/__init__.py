from io_files.dataclass import ProblemData, Ride, SolutionData


def user_has_not_provided_arguments(args):
    return len(args) <= 2

def get_ride_from_line(line: str, line_number: int):
    line = line.split(" ")
    return Ride(
        idx=line_number,
        start=[int(line[0]), int(line[1])],
        finish=[int(line[2]), int(line[3])],
        earliest_start=int(line[4]),
        latest_finish=int(line[5]),
    )
    

def read_file(filename: str) -> ProblemData:
    file_content = open(filename, 'r').read()
    lines = file_content.split("\n")
    line_1 = lines[0].split(" ")
    rides = [ get_ride_from_line(lines[i], i-1) for i in range(1, len(lines)-1) ]
    
    return ProblemData(
        rows=int(line_1[0]),
        columns=int(line_1[1]),
        vehicles=int(line_1[2]),
        number_of_rides=int(line_1[3]),
        bonus=int(line_1[4]),
        steps=int(line_1[5]),
        rides=rides,
    )

def write_submission(data: SolutionData) -> str:
    solution = f"Points: {data.points}\n\n"
    
    for index, vehicle in enumerate(data.vehicles):
        solution += f"{index+1} "
        solution += " ".join([str(i) for i in vehicle.rides])
        solution += "\n"
        
    return solution