# LeetCode 0023 - Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap: list[tuple[int, int, ListNode]] = []
        counter = 0

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1

        dummy = ListNode()
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next
