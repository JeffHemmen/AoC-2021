import part2

def test_with_example_input():
    with open('test.1.input.txt', 'r') as f:
        input = [(instr, int(n)) for cmd in f.read().split('\n') for instr, n in [cmd.split()]]
    assert part2.main(input) == 900
