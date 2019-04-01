#!bin/env python3
import argparse
from pathlib import Path

# USAGE: pearch some_log.txt content.
# Search content inside some_log.txt if no content provided, return everything.

# TODO: ADD A try:except
# TODO: ADD line numbers as a argument option.
# TODO: ADD highlight color to result.
# TODO: Search and replace feature.
    #TODO: ADD write feature to replace.

# argparse init and settings.
def parsed():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='input file to be pearched',required=True)
    parser.add_argument('--pattern', help='search for a specific pattern')
    parser.add_argument('--l', help='add line numbers to result', action='store_true' )
    parser.add_argument('--replace', help='replace pattern')
    args = parser.parse_args()

    # These will become a tuple to be unpacked later in the main loop.
    return args.file, args.pattern, args.l, args.replace

# pearch main function.
def pearch(file, pattern , list_num, replace):

    # open the recieved file input.
    with open(file, 'r') as reader:
        # if a pattern is given run this logic.
        if bool(pattern):
            # if --replace input is given, replace the pattern with the input.
            if bool(replace):
                 result = [line.replace(pattern, replace) for line in reader.readlines() if pattern in line]
                 print(result)
            # if no --replace pattern given just print the pattern
            else:
                result = [line for line in reader.readlines() if pattern in line]
                print(result)
        # if no pattern is given run this logic.
        # if --l option is toggled run this logic which also prints line numbers.
        if list_num == True:
            for i, line in enumerate(reader): print(f'{i}: {line}', end="")
        # if no other options is given just print the whole file.
        else:
            for line in reader: print(line, end="")


def main():
    # unpack parsed tuples to the variable to be sent to pearched.
    file, pattern, list_num, replace = parsed()
    pearch(file, pattern, list_num, replace)



if __name__ == '__main__':
    main()
