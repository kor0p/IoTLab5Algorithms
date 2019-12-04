import sys

def main(file):
    with open(file) as f:
        width, height = map(int, f.readline().split())
        field = tuple(map(''.join, zip(*(f.readline()[:-1] for _ in range(height)))))
    print(width, height)
    print(*tuple(map(''.join, zip(*field))), sep='\n')

    sumField = [[0]*height for _ in range(width)]
    sumField[-1][0] = sumField[-1][-1] = 1
    for w in range(width-2, -1, -1):
        for h in range(height):
            sumField[w][h] = sum((
                sumField[j][i]
                for i in range(height)
                for j in range(w+1, width)
                if field[w][h] == field[j][i] or (i == h and j == w+1)
            ))
    return sum(sumField[0])

def test(file, res):
    N = main(file)
    assert N == res
    print(f'[TEST PASSED] N: {N}')


test('inp1', 5)
test('inp2', 2)
test('inp3', 201684)
test('inp4', 14)
print('ALL TESTS PASSED\nYOUR EXAMPLE:')
test(sys.argv[1], int(sys.argv[2]))
