# LeetCode 3863 - Minimum Operations To Sort A String
# https://leetcode.com/problems/minimum-operations-to-sort-a-string/


class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        sorted_ok = True
        for i in range(1, n):
            if s[i] < s[i - 1]:
                sorted_ok = False
                break
        if sorted_ok:
            return 0
        if n == 2:
            return -1
        mn = s[0]
        mx = s[0]
        for c in s:
            if c < mn:
                mn = c
            if c > mx:
                mx = c
        if s[0] == mn or s[n - 1] == mx:
            return 1
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2
        return 3
