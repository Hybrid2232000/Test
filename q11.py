class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solution(root, p, q):
    stack = [root]
    parent = {root: None}
    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]
    while q not in ancestors:
        q = parent[q]
    return q


root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(11)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(2)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.right = TreeNode(11)

print(solution(root, root.left.left, root.left.right).val)