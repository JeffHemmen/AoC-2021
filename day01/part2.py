#!/usr/bin/env python3

def main(input):
    count = 0
    windows = [sum(input[n:3]) for n in range(3)]
    # windows = [
    #     sum(input[0:3]),
    #     sum(input[1:3]),
    #     input[2]]
    for i, v in enumerate(input[3:]):
        i1 = i % 3
        i2 = (i1 + 1) % 3
        i3 = (i1 + 2) % 3
        windows[i2] += v
        windows[i3] += v
        if windows[i2] > windows[i1]:
            count += 1
        windows[i1] = v
    return count


if __name__ == '__main__':
    with open('part1.input', 'r') as f:
        input = [int(x) for x in f.read().split()]
        print(main(input))