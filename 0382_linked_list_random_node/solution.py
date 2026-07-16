# LeetCode 0382 - Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/

import random
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head: list[int] | ListNode | None):
        if isinstance(head, list):
            head = self._build_list(head)
        self.nodes: list[ListNode] = []
        current = head
        while current:
            self.nodes.append(current)
            current = current.next
        random.seed(327)

    def _build_list(self, values: list[int]) -> ListNode | None:
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def getRandom(self) -> int:
        return random.choice(self.nodes).val
