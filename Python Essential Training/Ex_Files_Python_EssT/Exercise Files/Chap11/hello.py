#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


class MyString(str):
    def __str__(self):
        return self[::-1]



x = ('Hello, World {}'.upper().format(34*8))
print(x)
