#!/usr/bin/env python3

def main(input):
    a, h, d = 0, 0, 0
    for instr, n in input:
        if instr == 'down':
            a += n
        elif instr == 'up':
            a -= n
        elif instr == 'forward':
            h += n
            d += n * a
    return h * d

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [(instr, int(n)) for cmd in f.read().split('\n') for instr, n in [cmd.split()]]
        print(main(input))