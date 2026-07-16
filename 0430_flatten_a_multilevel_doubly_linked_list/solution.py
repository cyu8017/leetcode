# LeetCode 0430 - Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/


class Node:
    def __init__(
        self,
        val: int = 0,
        prev: "Node | None" = None,
        next: "Node | None" = None,
        child: "Node | None" = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: "Node | None") -> "Node | None":
        current = head
        while current:
            if current.child:
                next_node = current.next
                child_head = self.flatten(current.child)
                current.next = child_head
                child_head.prev = current
                tail = child_head
                while tail.next:
                    tail = tail.next
                tail.next = next_node
                if next_node:
                    next_node.prev = tail
                current.child = None
            current = current.next
        return head
