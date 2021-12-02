import part1

def test_with_example_input():
    with open('test.1.input.txt', 'r') as f:
        input = [(instr, int(n)) for cmd in f.read().split('\n') for instr, n in [cmd.split()]]
    assert part1.main(input) == 150
