# LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

from typing import List


class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda it: -it[0])
        seen = set()
        total = 0
        dup = []
        for i in range(k):
            total += items[i][0]
            c = items[i][1]
            if c in seen:
                dup.append(items[i][0])
            else:
                seen.add(c)
        ans = total + len(seen) * len(seen)
        for i in range(k, len(items)):
            c = items[i][1]
            if c in seen or not dup:
                continue
            total += items[i][0] - dup.pop()
            seen.add(c)
            ans = max(ans, total + len(seen) * len(seen))
        return ans
