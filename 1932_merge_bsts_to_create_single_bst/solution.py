from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        value_to_root = {}
        count = {}
        for tree in trees:
            value_to_root[tree.val] = tree
            count[tree.val] = count.get(tree.val, 0) + 1
            if tree.left:
                count[tree.left.val] = count.get(tree.left.val, 0) + 1
            if tree.right:
                count[tree.right.val] = count.get(tree.right.val, 0) + 1

        roots = [t for t in trees if count[t.val] == 1]
        if len(roots) != 1:
            return None
        root = roots[0]

        def merge(node: TreeNode) -> bool:
            if not node:
                return True
            if node.left and node.left.val in value_to_root:
                node.left = value_to_root.pop(node.left.val)
            if node.right and node.right.val in value_to_root:
                node.right = value_to_root.pop(node.right.val)
            return merge(node.left) and merge(node.right)

        value_to_root.pop(root.val)
        if not merge(root) or value_to_root:
            return None

        def is_valid_bst(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return is_valid_bst(node.left, lo, node.val) and is_valid_bst(node.right, node.val, hi)

        return root if is_valid_bst(root, float('-inf'), float('inf')) else None
