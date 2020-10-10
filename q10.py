class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root):
    def dfs(root, x, y, num, dmin, dmax):
        if root:
            left = dfs(root.left, x - 1, y + 1, num * 2, dmin, dmax)
            right = dfs(root.right, x + 1, y + 1, 1 + num * 2, dmin, dmax)
            dmin[y] = min(num, dmin.get(y, float("inf")))
            dmax[y] = max(num, dmax.get(y, float("-inf")))
            return max(left or 0, right or 0, 1 + dmax[y] - dmin[y])
    return dfs(root, 0, 0, 1, {}, {})


root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(11)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(6)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.right = TreeNode(11)

print(solution(root))