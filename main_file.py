import sys
from arg_parser import create_parser
from file_generator import file_function
from validator import is_valid

if __name__ == '__main__':
    parser = create_parser()
    parameters = parser.parse_args(sys.argv[1:])


if is_valid(parameters) is True:
    file_function(parameters)
else:
    print(is_valid(parameters))
