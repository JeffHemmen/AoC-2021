#!/usr/bin/env python3

def main(input):
    raise NotImplementedError

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    print(main(input))