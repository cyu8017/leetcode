# LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
# https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

from typing import List


class Solution:
    def countNonDecreasingArrays(self, digitSum: List[int]) -> int:
        mod = 1000000007
        groups: List[List[int]] = [[] for _ in range(51)]
        for x in range(5001):
            s = 0
            y = x
            while y > 0:
                s += y % 10
                y //= 10
            groups[s].append(x)
        prev_vals = groups[digitSum[0]]
        dp = [1] * len(prev_vals)
        for pos in range(1, len(digitSum)):
            cur_vals = groups[digitSum[pos]]
            nxt = [0] * len(cur_vals)
            j = 0
            prefix = 0
            for i in range(len(cur_vals)):
                x = cur_vals[i]
                while j < len(prev_vals) and prev_vals[j] <= x:
                    prefix += dp[j]
                    if prefix >= mod:
                        prefix -= mod
                    j += 1
                nxt[i] = prefix
            prev_vals = cur_vals
            dp = nxt
        ans = 0
        for x in dp:
            ans += x
            if ans >= mod:
                ans -= mod
        return ans
