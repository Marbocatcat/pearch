#!bin/env python3
import argparse
from pathlib import Path
from colorama import init, Fore, Back, Style

init(autoreset=True)

# USAGE: pearch some_log.txt content.
# Search content inside some_log.txt if no content provided, return everything.
# Highlight the pattern given.
# Add a search and replace feature.

# TODO: ADD A try:except
# TODO: ADD line numbers as a argument option.

def parsed():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)
    parser.add_argument('--pattern')
    args = parser.parse_args()

    return args.file, args.pattern

def pearch(file, pattern):

    with open(file, 'r') as reader:
        if bool(pattern):
            result = [line for line in reader.readlines() if pattern in line]
            print(result)
        else:
            for i, line in enumerate(reader): print(f'{i}: {line}', end="")


def main():
    file, pattern = parsed()
    pearch(file, pattern)



if __name__ == '__main__':
    main()
