#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(1,3,4)
    x = 5 
    print (id(x))
    
def kitten(a,b,c):
    print ('Meow.')
    print(a,b,c)

if __name__ == '__main__': main()
