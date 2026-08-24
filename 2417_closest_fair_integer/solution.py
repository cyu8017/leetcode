# LeetCode 2417 - Closest Fair Integer
# https://leetcode.com/problems/closest-fair-integer/

class Solution:
    def closestFair(self, n: int) -> int:
        x = n
        while True:
            s = str(x)
            if len(s) % 2 != 0:
                p = 1
                for _ in s:
                    p *= 10
                return self.closestFair(p)
            even = odd = 0
            for c in s:
                if (ord(c) - 48) % 2 == 0:
                    even += 1
                else:
                    odd += 1
            if even == odd:
                return x
            x += 1
