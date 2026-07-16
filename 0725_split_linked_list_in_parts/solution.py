# LeetCode 0725 - Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/

from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        part_size, extra = divmod(length, k)
        result: list[Optional[ListNode]] = []
        current = head
        for i in range(k):
            result.append(current)
            size = part_size + (1 if i < extra else 0)
            for _ in range(size - 1):
                if current:
                    current = current.next
            if current:
                nxt = current.next
                current.next = None
                current = nxt
        return result
