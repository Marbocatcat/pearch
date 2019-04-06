#/bin/env python3

import argparse
import pathlib
import fileinput

'''
    Name: pearch
    Usage: pearch --file some_file --pattern some_pattern --replace
    Description: a tool similar to the popular UNIX command "grep/cat"
    
    Main Features:
        1. Print the file input as default behavior.
        2. with "--pattern" print the line with the pattern provided.
        3. with "--replace", "--pattern" is needed.

'''


class Pearch:
    
    def __init__(self, file):
        self.file = file
    
    def print_file(self):
        return_file = str(self.file)
        return f"File Path: {return_file}"
    
    def printer(self):
        with open(self.file, "r") as reader:
            result = [line.strip() for line  in reader.readlines()]
            
            for i, lines in enumerate(result):
                print(lines)
                
    def print_pattern(self, target):
        with open(self.file, "r") as reader:
            result = [line for line in reader.readlines() if target in line]
            print(result)
            
    def print_replace(self, target, pattern):
        with fileinput.FileInput(self.file, inplace=True, backup=".bak") as file:
            for line in file:
                print(line.replace(target, pattern), end="")




def main():
    
    def parse_args():
        
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", required=True)
        parser.add_argument("--target")
        parser.add_argument("--pattern")
        args = parser.parse_args()

        return args.file, args.target, args.pattern
        
    
    
    def switch(file, target, pattern):
        
        pearch = Pearch(file)
        
        if bool(target) and bool(pattern):
            pearch.print_replace(target, pattern)
        elif bool(target):
            pearch.print_pattern(target)
        else:
            pearch.printer()
    
    
    file, target, pattern = parse_args()
    switch(file, target, pattern)
    

    
if __name__ == "__main__":
    main()