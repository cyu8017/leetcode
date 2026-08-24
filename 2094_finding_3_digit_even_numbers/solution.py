# LeetCode 2094 - Finding 3-Digit Even Numbers
# https://leetcode.com/problems/finding-3-digit-even-numbers/

from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0] * 10
        for d in digits:
            freq[d] += 1
        ans = []
        for x in range(100, 999, 2):
            a, b, c = x // 100, (x // 10) % 10, x % 10
            freq[a] -= 1
            freq[b] -= 1
            freq[c] -= 1
            if freq[a] >= 0 and freq[b] >= 0 and freq[c] >= 0:
                ans.append(x)
            freq[a] += 1
            freq[b] += 1
            freq[c] += 1
        return ans
