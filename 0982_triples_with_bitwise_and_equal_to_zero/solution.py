# LeetCode 0982 - Triples with Bitwise AND Equal To Zero
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/

from collections import Counter


class Solution:
    def countTriplets(self, nums: list[int]) -> int:
        cnt: Counter[int] = Counter()
        for a in nums:
            for b in nums:
                cnt[a & b] += 1
        ans = 0
        for c in nums:
            for ab, times in cnt.items():
                if ab & c == 0:
                    ans += times
        return ans
