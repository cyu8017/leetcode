# LeetCode 2844 - Minimum Operations to Make a Special Number
# https://leetcode.com/problems/minimum-operations-to-make-a-special-number/


class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        ans = n
        if "0" in num:
            ans = min(ans, n - 1)
        for t in ("00", "25", "50", "75"):
            j = n - 1
            while j >= 0 and num[j] != t[1]:
                j -= 1
            if j < 0:
                continue
            i = j - 1
            while i >= 0 and num[i] != t[0]:
                i -= 1
            if i < 0:
                continue
            ans = min(ans, n - i - 2)
        return ans
