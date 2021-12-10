#!/usr/bin/env python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['A', 'B'])



def is_horizontal(line):
    pass

def is_vertical(line):
    pass

def parse_lines(filename):
    pass

def get_points(line):
    pass
Line.points = get_points # monkey-patch as method


def main(filename):
    pass


if __name__ == '__main__':
    pass