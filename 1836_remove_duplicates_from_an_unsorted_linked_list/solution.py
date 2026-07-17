# LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

from collections import Counter


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode | None) -> ListNode | None:
        counts: Counter[int] = Counter()
        node = head
        while node:
            counts[node.val] += 1
            node = node.next

        dummy = ListNode(0, head)
        prev = dummy
        node = head
        while node:
            if counts[node.val] > 1:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next
        return dummy.next
