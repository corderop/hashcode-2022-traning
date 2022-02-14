import sys

from io_files import read_file, user_has_not_provided_arguments, write_submission
from algorithm import process_data

if __name__ == "__main__":
    arguments = sys.argv
    
    if user_has_not_provided_arguments(arguments):
        exit("User has not provided filename")
        
    filename = arguments[1]
    data = read_file(filename)
    solution = process_data(data)
    print(write_submission(solution))
