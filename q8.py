def is_valid(board, r, c):
    # check row
    row_used_val = set()
    for v in board[r]:
        if v == '.':
            continue
        if v not in row_used_val:
            row_used_val.add(v)
        else:
            return False
    # check column
    col_used_val = set()
    for row in board:
        v = row[c]
        if v == '.':
            continue
        if v not in col_used_val:
            col_used_val.add(v)
        else:
            return False
    # check box
    box_used_val = set()
    for i in range(r//3*3, r//3*3+3):
        for j in range(c//3*3, c//3*3+3):
            v = board[i][j]
            if v == '.':
                continue
            if v not in box_used_val:
                box_used_val.add(v)
            else:
                return False
    return True


def backtrack(board, q, pos):
    if pos == len(q):
        return True
    r, c = q[pos]
    for k in range(1, 10):
        board[r][c] = str(k)
        if is_valid(board, r, c) and backtrack(board, q, pos+1):
            return True
        board[r][c] = '.'
    return False


def get_empty(board):
    q = []
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == '.':
                q.append((i, j))
    return q


def solution(board) -> None:
    q = get_empty(board)
    # back tracking.
    backtrack(board, q, 0)

board = [['1','.','.','.','.','.','.','.','.'],['2','.','.','.','.','.','.','.','.'],['3','.','.','.','.','.','.','.','.'],['4','.','.','.','.','.','.','.','.'],['5','.','.','.','.','.','.','.','.'],['6','.','.','.','.','.','.','.','.'],['7','.','.','.','.','.','.','.','.'],['8','.','.','.','.','.','.','.','.'],['9','.','.','.','.','.','.','.','.']]
solution(board)
for i in board:
    print(i)