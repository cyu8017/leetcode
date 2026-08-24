# LeetCode 2125 - Number of Laser Beams in a Bank
# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for row in bank:
            cnt = 0
            for i in range(len(row)):
                if row[i] == "1":
                    cnt += 1
            if cnt > 0:
                ans += prev * cnt
                prev = cnt
        return ans
