#!/usr/bin/env python3

def main(input):
    count, last = 0, input[0]
    for v in input[1:]:
        if v > last:
            count += 1
        last = v
    return count

if __name__ == '__main__':
    with open('part1.input', 'r') as f:
        input = [int(x) for x in f.read().split()]
        print(main(input))