# LeetCode 2375 - Construct Smallest Number From DI String
# https://leetcode.com/problems/construct-smallest-number-from-di-string/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        ans = [chr(49 + i) for i in range(n + 1)]
        i = 0
        while i < n:
            if pattern[i] == "I":
                i += 1
                continue
            j = i
            while j < n and pattern[j] == "D":
                j += 1
            l, r = i, j
            while l < r:
                ans[l], ans[r] = ans[r], ans[l]
                l += 1
                r -= 1
            i = j
        return "".join(ans)
