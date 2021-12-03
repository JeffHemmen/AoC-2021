import part2

def test_with_example_input():
    with open('test.1.input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    assert part2.main(input) == 230

def test_oxygen_generator_rating():
    with open('test.1.input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    assert part2.calculate_rating(input, 1) == 23

def test_CO2_scrubber_rating():
    with open('test.1.input.txt', 'r') as f:
        input = [line for line in f.read().split()]
    assert part2.calculate_rating(input, 0) == 10