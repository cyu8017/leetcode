# LeetCode 1530

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root, distance):
        answer = 0
        def dfs(node):
            nonlocal answer
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            left, right = dfs(node.left), dfs(node.right)
            answer += sum(a + b <= distance for a in left for b in right)
            return [depth + 1 for depth in left + right if depth + 1 < distance]
        dfs(root)
        return answer
