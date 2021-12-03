import part2

def test_with_example_input():
    with open('test.1.input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    assert part2.main(input) == 230