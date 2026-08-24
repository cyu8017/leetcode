# LeetCode 2171 - Removing Minimum Number of Magic Beans
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

from typing import List
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans = sorted(beans)
        n = len(beans)
        sum = 0
        for b in beans:
            sum += b
        ans = sum
        for i in range(n):
            remain = (n - i) * beans[i]
            ans = min(ans, sum - remain)
        return ans
