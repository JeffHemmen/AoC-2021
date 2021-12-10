#!/usr/bin/env python3

from collections import namedtuple, defaultdict

Point = namedtuple('Point', ['x', 'y'])
Line = namedtuple('Line', ['A', 'B'])



def is_horizontal(line):
    return line.A.y == line.B.y

def is_vertical(line):
    return line.A.x == line.B.x

def parse_lines(filename):
    lines = []
    with open(filename, 'r') as f:
        filelines = f.read().split('\n')
    for fileline in filelines:
        Aline, Bline = fileline.split(' -> ')
        A, B = Point(*[int(s) for s in Aline.split(',')]), Point(*[int(s) for s in Bline.split(',')])
        lines.append(Line(A, B))
    return lines

def get_points(line):
    if is_horizontal(line):
        minx, maxx = min(line.A.x, line.B.x), max(line.A.x, line.B.x) + 1
        return [Point(x, line.A.y) for x in range(minx, maxx)]
    elif is_vertical(line):
        miny, maxy = min(line.A.y, line.B.y), max(line.A.y, line.B.y) + 1
        return [Point(line.A.x, y) for y in range(miny, maxy)]
    else:
        raise NotImplementedError

Line.points = get_points # monkey-patch as method


def main(filename):
    lines = parse_lines(filename)
    points = defaultdict(lambda: 0)
    for line in lines:
        if not is_vertical(line) and not is_horizontal(line):
            continue
        for point in line.points():
            points[point] += 1
    
    result = 0
    for num_lines in points.values():
        if num_lines >= 2:
            result += 1
    return result


if __name__ == '__main__':
    print(main('input.txt'))