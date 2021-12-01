import part1

def test_with_example_input_1():
    with open('test.1.part1.input', 'r') as f:
        inputs = [int(x) for x in f.read().split()]
        assert part1.main(inputs) == 7