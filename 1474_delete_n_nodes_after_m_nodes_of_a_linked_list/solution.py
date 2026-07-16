from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val, self.next = val, next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        cur = head
        while cur:
            for _ in range(m - 1):
                if not cur:
                    break
                cur = cur.next
            if not cur:
                break
            drop = cur.next
            for _ in range(n):
                if drop:
                    drop = drop.next
            cur.next = drop
            cur = drop
        return head
