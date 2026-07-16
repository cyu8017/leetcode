# LeetCode 0109 - Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            mid = (left + right + 1) // 2
            root = TreeNode(values[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(values) - 1)
