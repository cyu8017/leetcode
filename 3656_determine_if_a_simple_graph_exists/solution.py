# LeetCode 3656 - Determine if a Simple Graph Exists
# https://leetcode.com/problems/determine-if-a-simple-graph-exists/

from typing import List


class Solution:
    def simpleGraphExists(self, degrees: List[int]) -> bool:
        n = len(degrees)
        d = sorted(degrees, reverse=True)
        total = 0
        for x in d:
            if x < 0 or x >= n:
                return False
            total += x
        if total % 2 == 1:
            return False
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + d[i]
        for k in range(1, n + 1):
            right = 0
            for i in range(k, n):
                right += d[i] if d[i] < k else k
            if prefix[k] > k * (k - 1) + right:
                return False
        return True
