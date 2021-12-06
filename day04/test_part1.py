import part1

draws, sheets = part1.load_input('test.1.input.txt')

def test_draws():
    assert draws == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

def test_sheets():
    assert len(sheets) == 3
    
    for sheet in sheets:
        assert len(sheet) == 5
        for row in sheet:
            assert len(row) == 5


def test_end_result():
    assert part1.main('test.1.input.txt') == 4512


def test_check_winner():
    sheet = [
        [1, 2, None, 4, 5],
        [1, 2, None, 4, 5],
        [1, 2, None, 4, 5],
        [1, 2, None, 4, 5],
        [1, 2, None, 4, 5],
    ]
    assert part1.check_winner([sheet]) is sheet