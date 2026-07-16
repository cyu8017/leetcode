# LeetCode 0970 - Powerful Integers
# https://leetcode.com/problems/powerful-integers/

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        ans = set()
        a = 1
        while a < bound:
            b = 1
            while a + b <= bound:
                ans.add(a + b)
                if y == 1:
                    break
                b *= y
            if x == 1:
                break
            a *= x
        return list(ans)
