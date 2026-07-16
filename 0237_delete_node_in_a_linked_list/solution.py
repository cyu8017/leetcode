# LeetCode 0237 - Delete Node in a Linked List
# https://leetcode.com/problems/delete-node-in-a-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        node.val = node.next.val
        node.next = node.next.next
