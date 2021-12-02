#!/usr/bin/env python3

def main(input):
    return NotImplementedError

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [(instr, int(n)) for cmd in f.read().split('\n') for instr, n in [cmd.split()]]
        print(main(input))