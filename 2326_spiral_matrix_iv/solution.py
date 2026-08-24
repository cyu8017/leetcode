# LeetCode 2326 - Spiral Matrix IV
# https://leetcode.com/problems/spiral-matrix-iv/

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = c = d = 0
        while head is not None:
            ans[r][c] = head.val
            head = head.next
            nr, nc = r + dirs[d][0], c + dirs[d][1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or ans[nr][nc] != -1:
                d = (d + 1) % 4
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            r, c = nr, nc
        return ans
