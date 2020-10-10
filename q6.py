def place_queen(diag1, diag2, cols, row, col):
    diag1.add(row + col)
    diag2.add(row - col)
    cols[col] = row

def remove_queen(diag1, diag2, cols, row, col):
    diag1.remove(row + col)
    diag2.remove(row - col)
    del cols[col]

def is_under_attack(diag1, diag2, cols, row, col):
    return row + col in diag1 or row - col in diag2 or col in cols

def backtrack(diag1, diag2, cols, n, row, res, pos):
    for col in range(n):
        if not is_under_attack(diag1, diag2, cols, row, col):
            place_queen(diag1, diag2, cols, row, col)
            if row == n - 1:
                res.append([j * '_ ' + 'Q ' + (n - 1 - j) * '_ ' for j in pos + [col]])
            else:
                backtrack(diag1, diag2, cols, n, row + 1, res, pos + [col])
            remove_queen(diag1, diag2, cols, row, col)

def solution(n):
    diag_set1 = set()
    diag_set2 = set()
    col_map = {}
    res_list = []
    backtrack(diag_set1, diag_set2, col_map, n, 0, res_list, [])
    return res_list

ans = solution(4)

for i in ans:
    for j in i:
        print(j)
    print("========")