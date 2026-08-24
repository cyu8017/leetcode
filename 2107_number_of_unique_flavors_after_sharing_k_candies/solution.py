# LeetCode 2107 - Number of Unique Flavors After Sharing K Candies
# https://leetcode.com/problems/number-of-unique-flavors-after-sharing-k-candies/

from typing import List


class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        n = len(candies)
        freq = {}
        for c in candies:
            freq[c] = freq.get(c, 0) + 1
        if k == 0:
            return len(freq)
        for i in range(k):
            c = candies[i]
            v = freq[c] - 1
            if v == 0:
                del freq[c]
            else:
                freq[c] = v
        ans = len(freq)
        for i in range(k, n):
            freq[candies[i - k]] = freq.get(candies[i - k], 0) + 1
            c = candies[i]
            v = freq[c] - 1
            if v == 0:
                del freq[c]
            else:
                freq[c] = v
            ans = max(ans, len(freq))
        return ans
