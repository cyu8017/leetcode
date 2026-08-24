# LeetCode 2678 - Number of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            age = (ord(d[11]) - 48) * 10 + (ord(d[12]) - 48)
            if age > 60:
                ans += 1
        return ans
