#!bin/env python3
import argparse
from pathlib import Path


'''
    NAME:   pearch
    USAGE:  pearch --file file.txt
    DESCRIPTION:  a combination of the grep/cat UNIX command
'''


# TODO: ADD A try:except
# TODO: ADD line numbers as a argument option.
# TODO: ADD highlight color to result.
# TODO: Search and replace feature.
    #TODO: ADD write feature to replace.


# argparse settings
def parsed():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='input file to be pearched',required=True)
    parser.add_argument('--pattern', help='search for a specific pattern')
    parser.add_argument('--l', help='add line numbers to result', action='store_true' )
    parser.add_argument('--replace', help='replace pattern')
    args = parser.parse_args()

    # These will become a tuple to be unpacked later in the main loop
    return args.file, args.pattern, args.l, args.replace


# main logic loop
def pearch(file, pattern , list_num, replace):

    with open(file, 'r') as reader:
        if bool(pattern):   # --pattern
            if bool(replace):   # --replace
                # NEED TO WORK ON WRITE LOGIC BELOW!
                result = [reader.write(line.replace(pattern, replace)) for line in reader.readlines() if pattern in line]
                print(result)
            else:
                # if pattern is in the file print the pattern(list)
                result = [line for line in reader.readlines() if pattern in line]
                print(result)
        if list_num == True:    # --l
            for i, line in enumerate(reader): print(f'{i}: {line}', end="")
        else:
            # print line with no options
            for line in reader: print(line, end="")


def main():
    # unpack parsed tuples to the variable and give to pearch function
    file, pattern, list_num, replace = parsed()
    pearch(file, pattern, list_num, replace)


if __name__ == '__main__':
    main()
