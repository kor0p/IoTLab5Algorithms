with open('input') as f:
    W, H = map(int, f.readline().split())
    field = tuple(map(''.join, zip(*(f.readline()[:-1] for _ in range(H)))))
#transpose_field = tuple((f.readline()[:-1] for h in range(H)))
#field = tuple(map(''.join, zip(*transpose_field)))

sumField = [[0]*H for _ in range(W)]
sumField[-1][0] = sumField[-1][-1] = 1
for w in range(W-2, -1, -1):
    for h in range(H):
        sumField[w][h] = sum((
            sumField[j][i]
            for i in range(H)
            for j in range(w+1, W)
            if field[w][h] == field[j][i] or (i == h and j == w+1)
        ))
print('N: ', sum(sumField[0]))
