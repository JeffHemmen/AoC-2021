#!/usr/bin/env python3

def main(input):
    sumbits = [0] * len(input[0])
    for bits in input:
        for i, b in enumerate(bits):
            if b == '1':
                sumbits[i] += 1
    # print(sumbits)
    # GAMMA - MOST COMMON BITS
    gamma, epsilon = 0, 0
    n = len(input)
    for pwr, bit in enumerate(reversed(sumbits)):
        if bit > n / 2: # most common bit 1
            gamma += 2 ** pwr
        else:
            epsilon += 2 ** pwr
    return epsilon * gamma

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    print(main(input))