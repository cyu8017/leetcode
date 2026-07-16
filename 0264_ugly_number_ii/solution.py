# LeetCode 0264 - Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        index2 = index3 = index5 = 0
        while len(ugly) < n:
            next_ugly = min(
                ugly[index2] * 2,
                ugly[index3] * 3,
                ugly[index5] * 5,
            )
            ugly.append(next_ugly)
            if next_ugly == ugly[index2] * 2:
                index2 += 1
            if next_ugly == ugly[index3] * 3:
                index3 += 1
            if next_ugly == ugly[index5] * 5:
                index5 += 1
        return ugly[-1]
