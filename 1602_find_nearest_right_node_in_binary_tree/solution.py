class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val, self.left, self.right = val, left, right
    def __eq__(self, other): return self.val == (other.val if hasattr(other, "val") else other)
class Solution:
    def findNearestRightNode(self, root, u):
        target = u.val if hasattr(u, "val") else u
        q = [root] if root else []
        while q:
            nxt = []
            for i, node in enumerate(q):
                if node.val == target:
                    ans = q[i + 1] if i + 1 < len(q) else None
                    return ans.val if ans and not hasattr(u, "val") else ans
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
            q = nxt
