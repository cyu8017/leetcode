# LeetCode 2597 - The Number of Beautiful Subsets
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1
        groups = {}
        for key in freq:
            rem = key % k
            if rem not in groups:
                groups[rem] = []
            groups[rem].append(key)
        ans = 1
        for vals in groups.values():
            vals.sort()
            prev_take = 0
            prev_skip = 1
            prev_val = float("-inf")
            for v in vals:
                ways = 1
                for _ in range(freq[v]):
                    ways *= 2
                ways -= 1
                skip = prev_take + prev_skip
                take = ways * prev_skip
                if prev_val + k != v:
                    take += ways * prev_take
                prev_take = take
                prev_skip = skip
                prev_val = v
            ans *= prev_take + prev_skip
        return ans - 1
