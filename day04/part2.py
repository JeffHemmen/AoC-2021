#!/usr/bin/env python3

def load_input(fn):
    with open(fn, 'r') as f:
        lines = f.read().split('\n')
    draws = [int(n) for n in lines[0].split(',')]
    sheets = []
    for line in lines[1:]:
        if line == '':
            sheets.append([])
            continue
        sheets[-1].append([int(n) for n in line.split()])
    
    return draws, sheets

def check_winner(sheets):
    for sheet in sheets:
        for row in sheet:
            if all(x is None for x in row):
                return sheet
        # assume sheet is always 5x5
        for col in range(5):
            if all(sheet[row][col] is None for row in range(5)):
                return sheet
    return None

def calculate_score(winner, d):
    sum = 0
    for row in winner:
        for n in row:
            sum += n if n else 0
    return sum * d

def debug_print_sheets(sheets):
    print('='*5, format(len(sheets)), 'sheets', '='*5)
    for sheet in sheets:
        for row in sheet:
            print('%3d %3d %3d %3d %3d' % tuple([n if n is not None else -1 for n in row]))
        print()


def play_bingo_to_lose(draws, sheets):
    for d in draws:
        for sheet in sheets:
            for row in range(5):
                for col in range(5):
                    if sheet[row][col] == d:
                        sheet[row][col] = None

        for sheet in sheets:
            if check_winner([sheet]):
                if len(sheets) == 1:
                    # loser won
                    # print(sheet, d)
                    score = calculate_score(sheet, d)
                    return(score)
                sheets.remove(sheet)


def main(fn):
    draws, sheets = load_input(fn)
    score = play_bingo_to_lose(draws, sheets)
    return score


if __name__ == '__main__':
    print(main('input.txt'))