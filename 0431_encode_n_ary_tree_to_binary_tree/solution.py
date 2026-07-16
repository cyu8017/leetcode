# LeetCode 0431 - Encode N-ary Tree to Binary Tree
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/


class Node:
    def __init__(self, val: int | None = None, children: list["Node"] | None = None):
        self.val = val
        self.children = children if children is not None else []


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def encodeNaryTree(self, root: "Node | None") -> TreeNode | None:
        if root is None:
            return None
        binary = TreeNode(root.val)
        if not root.children:
            return binary
        binary.left = self.encodeNaryTree(root.children[0])
        sibling = binary.left
        for child in root.children[1:]:
            sibling.right = self.encodeNaryTree(child)
            sibling = sibling.right
        return binary

    def decodeBinaryTree(self, root: TreeNode | None) -> Node | None:
        if root is None:
            return None
        node = Node(root.val, [])
        current = root.left
        while current:
            node.children.append(self.decodeBinaryTree(current))
            current = current.right
        return node
