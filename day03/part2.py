#!/usr/bin/env python3

def to_decimal(binstr):
    res = 0
    for pwr, bit in enumerate(reversed(binstr)):
        if bit == '1':
            res += 2 ** pwr
    return res

def calculate_rating(input, bit_criteria):
    # bit criteria == 1 => most  common, else 1
    # bit criteria == 0 => least common, else 0
    s = sorted(input)
    idx, start, stop = 0, 0, len(input) - 1
    while start < stop:
        pivot = start
        # print(start, stop)
        while s[pivot][idx] != '1' and pivot <= stop:
            pivot += 1
        # balance > 0 => more 0s than 1s
        # balance < 0 => more 1s than 0s
        balance = (pivot - start) - (stop - pivot + 1)

        if bit_criteria == 1:
            if balance > 0:
                stop = pivot - 1
            else:
                start = pivot
        else:
            if balance <= 0:
                stop = pivot - 1
            else:
                start = pivot
        idx += 1
    return to_decimal(s[start])


def main(input):
    oxy = calculate_rating(input, 1)
    co2 = calculate_rating(input, 0)
    return oxy * co2

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    print(main(input))