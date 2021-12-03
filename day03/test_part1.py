import part1

def test_with_example_input():
    with open('input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    assert part1.main(input) == 198