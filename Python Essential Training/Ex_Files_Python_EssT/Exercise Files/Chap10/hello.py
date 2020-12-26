#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    try:
        x = 5/0
    except ZeroDivisionError:
        print("This is a value error")
    except ValueError:
        print('This is a value error')

    

if __name__ == '__main__': main()
