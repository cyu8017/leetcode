# LeetCode 0369 - Plus One Linked List
# https://leetcode.com/problems/plus-one-linked-list/


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode | None) -> ListNode | None:
        sentinel = ListNode(0, head)
        not_nine = sentinel
        node = head

        while node:
            if node.val != 9:
                not_nine = node
            node = node.next

        not_nine.val += 1
        node = not_nine.next
        while node:
            node.val = 0
            node = node.next

        return sentinel if sentinel.val == 1 else sentinel.next
