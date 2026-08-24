# LeetCode 3932 - Count K Th Roots In A Range
# https://leetcode.com/problems/count-k-th-roots-in-a-range/


class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1
        ans = 0
        x = 0
        while True:
            y = 1
            too_big = False
            for _i in range(k):
                if x != 0 and y > r // x:
                    too_big = True
                    break
                y *= x
                if y > r:
                    break
            if too_big or y > r:
                break
            if l <= y <= r:
                ans += 1
            x += 1
        return ans
