# LeetCode 0708 - Insert into a Sorted Circular Linked List
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

from typing import Optional


class Node:
    def __init__(self, val: int = 0, next: Optional["Node"] = None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: Optional[Node], insertVal: int) -> Node:
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        # Tests may pass a linear list; close it into a circle.
        cur = head
        while cur.next and cur.next is not head:
            cur = cur.next
        cur.next = head

        prev, curr = head, head.next
        while True:
            assert curr is not None
            if prev.val <= insertVal <= curr.val:
                break
            if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
                break
            prev, curr = curr, curr.next
            if prev is head:
                break

        prev.next = node
        node.next = curr
        return head
