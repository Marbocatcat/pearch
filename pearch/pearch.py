#!bin/env python3
import argparse
from pathlib import Path
from colorama import init, Fore, Back, Style

init(autoreset=True)

# USAGE: pearch some_log.txt content.
# Search content inside some_log.txt if no content provided, return everything.

# TODO: ADD A try:except
# TODO: ADD line numbers as a argument option.
# TODO: ADD highlight color to result.
# TODO: Search and replace feature.
    #TODO: ADD write feature to replace.

def parsed():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='input file to be pearched',required=True)
    parser.add_argument('--pattern', help='search for a specific pattern')
    parser.add_argument('--l', help='add line numbers to result', action='store_true' )
    parser.add_argument('--replace', help='replace pattern')
    args = parser.parse_args()

    return args.file, args.pattern, args.l, args.replace

def pearch(file, pattern , list_num, replace):

    with open(file, 'r') as reader:

        if bool(pattern):
            if bool(replace):
                 result = [line.replace(pattern, replace) for line in reader.readlines() if pattern in line]
                 print(result)
            else:
                result = [line for line in reader.readlines() if pattern in line]
                print(result)

        if list_num == True:
            for i, line in enumerate(reader): print(f'{i}: {line}', end="")
        else:
            for line in reader: print(line, end="")


def main():
    file, pattern, list_num, replace = parsed()
    pearch(file, pattern, list_num, replace)



if __name__ == '__main__':
    main()
