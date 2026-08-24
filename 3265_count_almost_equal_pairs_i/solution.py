# LeetCode 3265 - Count Almost Equal Pairs I
# https://leetcode.com/problems/count-almost-equal-pairs-i/

from typing import List


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        def sprintfNum(x: int) -> str:
            return str(x)

        def almostEqual(a: int, b: int) -> bool:
            sa, sb = sprintfNum(a), sprintfNum(b)
            while len(sa) < len(sb):
                sa = "0" + sa
            while len(sb) < len(sa):
                sb = "0" + sb
            diff = []
            for i in range(len(sa)):
                if sa[i] != sb[i]:
                    diff.append(i)
            if len(diff) == 0:
                return True
            if len(diff) != 2:
                return False
            i0, j = diff[0], diff[1]
            return sa[i0] == sb[j] and sa[j] == sb[i0]

        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if almostEqual(nums[i], nums[j]):
                    ans += 1
        return ans
