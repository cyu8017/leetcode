# LeetCode 3750 - Minimum Number of Flips to Reverse Binary String
# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution:
    def minimumFlips(self, n: int) -> int:
        x = n
        if x == 0:
            s = "0"
        else:
            bits = []
            while x > 0:
                bits.append(chr(48 + (x & 1)))
                x >>= 1
            s = "".join(reversed(bits))
        m = len(s)
        cnt = 0
        for i in range(m // 2):
            if s[i] != s[m - i - 1]:
                cnt += 1
        return cnt * 2
