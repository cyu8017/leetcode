# LeetCode 2217 - Find Palindrome With Fixed Length
# https://leetcode.com/problems/find-palindrome-with-fixed-length/

from typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half = (intLength + 1) >> 1
        start = 1
        for i in range(1, half):
            start *= 10
        total = start * 9
        ans = [None] * (len(queries))
        for i in range(len(queries)):
            q = queries[i]
            if q > total:
                ans[i] = -1
                continue
            left = start + q - 1
            pal = left
            x = left
            if intLength % 2 != 0:
                x = x // 10
            while x > 0:
                pal = pal * 10 + x % 10
                x = x // 10
            ans[i] = pal
        return ans
