#!/usr/bin/env pytest

from part1 import *

TEST_INPUT_FILE = 'test.1.input.txt'

p1 = Point(2, 3)
p2 = Point(2, 6)
p3 = Point(0, 6)
l1 = Line(p1, p2) # x = 2
l2 = Line(p2, p3) # y = 6
l3 = Line(p1, p3) # y = -3/2 x + 6

def test_horz_vert_lines():
    assert is_vertical(l1)
    assert is_horizontal(l2)
    assert not any([is_vertical(x) for x in [l2, l3]])
    assert not any([is_horizontal(x) for x in [l1, l3]])

def test_points_on_segment():
    assert all([Point(2, y) in l1.points() for y in range(3, 7)])
    assert not any([Point(2, y) in l1.points() for y in [0, 1, 7, 8]])
    assert all([Point(x, 6) in l2.points() for x in range(0, 3)])
    assert not any([Point(x, 6) in l2.points() for x in [-2, -1, 3, 4]])

def test_parse_lines():
    lines = parse_lines(TEST_INPUT_FILE)
    assert Line(Point(0,9), Point(5,9)) in lines
    assert Line(Point(5,5), Point(8,2)) in lines
    

def test_main():
    result = main(TEST_INPUT_FILE)
    assert result == 5

### Part 2

l4 = Line(Point(1, 1), Point(3, 3))
l5 = Line(Point(9, 7), Point(7, 9))

def test_points_on_diagonal():
    assert all([Point(x, x) in l4.points() for x in range(1, 4)])
    assert not any([Point(x, x) in l4.points() for x in [-1, 0, 4, 5]])
    assert all([Point(*p) in l5.points() for p in [(9,7), (8,8), (7,9)]])
    assert not any([Point(*p) in l5.points() for p in [(10,6), (6,10)]])


def test_main_part2():
    result = main(TEST_INPUT_FILE, ignore_diagonal=False)
    assert result == 12