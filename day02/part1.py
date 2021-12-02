#!/usr/bin/env python3

def main(input):
    h, d = 0, 0
    for instr, n in input:
        if instr == 'forward':
            h += n
        elif instr == 'down':
            d += n
        elif instr == 'up':
            d -= n
    return h*d

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [(instr, int(n)) for cmd in f.read().split('\n') for instr, n in [cmd.split()]]
        print(main(input))