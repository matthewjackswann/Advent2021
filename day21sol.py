# part 1

f = open("day21.txt","r")
player1Pos = int(f.readline()[28:])
player2Pos = int(f.readline()[28:])
f.close()

diceRolled = 0
player1Score = 0
player2Score = 0

def getDiceValue(roll):
    roll1 = (roll % 100) + 1
    roll2 = ((roll + 1) % 100) + 1
    roll3 = ((roll + 2) % 100) + 1
    return roll1 + roll2 + roll3

turn = 1
while player1Score < 1000 and player2Score < 1000:
    if turn == 1:
        turn = 2
        player1Pos = ((getDiceValue(diceRolled) + player1Pos - 1) % 10) + 1
        player1Score += player1Pos
    else:
        turn = 1
        player2Pos = ((getDiceValue(diceRolled) + player2Pos - 1) % 10) + 1
        player2Score += player2Pos
    diceRolled += 3

print(diceRolled*min(player1Score, player2Score))

# part 2

from functools import lru_cache

f = open("day21.txt","r")
player1Pos = int(f.readline()[28:])
player2Pos = int(f.readline()[28:])
f.close()

@lru_cache(maxsize=None)
def getWins(p1Score, p1Pos, p2Score, p2Pos, turn):
    if p1Score >= 21:
        return (1, 0)
    elif p2Score >= 21:
        return (0, 1)
    else:
        total1 = 0
        total2 = 0
        if turn == 1:
            for roll1 in range(1,3+1):
                for roll2 in range(1,3+1):
                    for roll3 in range(1,3+1):
                        newPos = ((roll1 + roll2 + roll3 + p1Pos - 1) % 10) + 1
                        x, y = getWins(p1Score + newPos, newPos, p2Score, p2Pos, 2)
                        total1 += x
                        total2 += y
        else:
            for roll1 in range(1,3+1):
                for roll2 in range(1,3+1):
                    for roll3 in range(1,3+1):
                        newPos = ((roll1 + roll2 + roll3 + p2Pos - 1) % 10) + 1
                        x, y = getWins(p1Score, p1Pos, p2Score + newPos, newPos, 1)
                        total1 += x
                        total2 += y
        return (total1, total2)

print(getWins(0, player1Pos, 0, player2Pos, 1))
