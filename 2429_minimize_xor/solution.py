# LeetCode 2429 - Minimize XOR
# https://leetcode.com/problems/minimize-xor/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = 0
        x = num2
        while x != 0:
            x &= x - 1
            bits += 1
        ans = 0
        for i in range(31, -1, -1):
            if bits <= 0:
                break
            if ((num1 >> i) & 1) != 0:
                ans |= 1 << i
                bits -= 1
        for i in range(32):
            if bits <= 0:
                break
            if ((ans >> i) & 1) == 0:
                ans |= 1 << i
                bits -= 1
        return ans
