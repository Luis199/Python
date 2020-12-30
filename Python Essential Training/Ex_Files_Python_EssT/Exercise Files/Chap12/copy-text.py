#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('/Users/luiscasado/Desktop/Python/Python Essential Training/Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'rt')
    outfile = open('/Users/luiscasado/Desktop/Python/Python Essential Training/Ex_Files_Python_EssT/Exercise Files/Chap12/lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
