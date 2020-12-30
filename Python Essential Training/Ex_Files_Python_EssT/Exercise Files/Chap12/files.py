#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('/Users/luiscasado/Desktop/Python/Python Essential Training/Ex_Files_Python_EssT/Exercise Files/Chap12/lines.txt', 'r')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
