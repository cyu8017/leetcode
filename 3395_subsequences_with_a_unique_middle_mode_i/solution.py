# LeetCode 3395 - Subsequences with a Unique Middle Mode I
# https://leetcode.com/problems/subsequences-with-a-unique-middle-mode-i/

from typing import List


class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        mod = 1000000007
        n = len(nums)
        ans = 0

        def uniqueMode(a: List[int]) -> bool:
            freq = {}
            for x in a:
                freq[x] = freq.get(x, 0) + 1
            best = 0
            cnt = 0
            for f in freq.values():
                if f > best:
                    best = f
                    cnt = 1
                elif f == best:
                    cnt += 1
            return cnt == 1

        for mid in range(2, n - 2):
            for a in range(mid):
                for b in range(a + 1, mid):
                    for c in range(mid + 1, n):
                        for d in range(c + 1, n):
                            if uniqueMode([nums[a], nums[b], nums[mid], nums[c], nums[d]]):
                                ans += 1
        return ans % mod
