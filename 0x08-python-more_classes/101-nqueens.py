#!/usr/bin/python3
"""Module finds all solutions for N queens problem"""


def solve(queens, size, start):
    """Recursive function to solve N queens problem
    Args:
        queens: number of queens to place
        size: size of board
    Returns True if valid move, False otherwise
    """
    if queens == 0:
        return True
    if start[0] >= size or start[1] >= size:
        return False
    x = start[0]
    y = start[1]
    if board[x][y] == 0 and isValid(x, y, size):
        board[x][y] = 1
        if solve(queens - 1, size, (x + 1, 0)):
            return True
        board[x][y] = 0
    return solve(queens, size, (x, y + 1))

#    for x in range(start[0], size):
#        for y in range(start[1], size):
#            if board[x][y] == 0 and isValid(x, y, size):
#                board[x][y] = 1
#                if solve(queens - 1, size, (x + 1, 0)):
#                    return True
#                board[x][y] = 0
#    return False


def isValid(x, y, size):
    """Returns whether a coordinate is valid and will not be attacked
    Args:
        x: x coordinate
        y: y coordinate
        size: size of board
    Returns True if valid coordinate, False otherwise
    """
    for i in range(size):
        if board[i][y] == 1 or board[x][i] == 1:
            return False
        dx = x + i
        dy = y + i
        if dx < size and dy < size and board[dx][dy] == 1:
            return False
        dx = x - i
        dy = y - i
        if dx > 0 and dy > 0 and board[dx][dy] == 1:
            return False

        for j in range(size):
            if i + j == x + y and board[i][j] == 1:
                return False
            if i - j == x - y and board[i][j] == 1:
                return False
    return True

if __name__ == "__main__":
    from sys import argv

    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    try:
        n = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    start = (0, 0)
    while start[1] < n:
        solutions = []
        board = [[0 for i in range(n)] for j in range(n)]
        if solve(n, n, start):
            for x in range(n):
                for y in range(n):
                    if board[x][y] == 1:
                        solutions.append([x, y])
            print(solutions)
            sy = solutions[0][1]
        else:
            sy = start[1]
        start = (0, sy + 1)
