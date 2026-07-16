# LeetCode 1054 - Distant Barcodes
# https://leetcode.com/problems/distant-barcodes/

from collections import Counter


class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        count = Counter(barcodes)
        n = len(barcodes)
        ans = [0] * n
        i = 0
        for value, freq in count.most_common():
            for _ in range(freq):
                ans[i] = value
                i += 2
                if i >= n:
                    i = 1
        return ans
