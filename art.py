numRows = int(input())
numCols = int(input())
numMoves = int(input())
map = []
for i in range(numRows):
    map.append([])
    for i2 in range(numCols):
        map[i].append(0)
#0 vs. 1 problem
moves = []
for i in range(numMoves):
    move = input().split(' ')
    moves.append({
        't' : move[0],
        'num': int(move[1])
    })
