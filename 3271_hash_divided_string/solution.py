# LeetCode 3271 - Hash Divided String
# https://leetcode.com/problems/hash-divided-string/

class Solution:
    def stringHash(self, s: str, k: int) -> str:
        out = []
        for i in range(0, len(s), k):
            ssum = 0
            for j in range(i, i + k):
                ssum += ord(s[j]) - 97
            out.append(chr(97 + ssum % 26))
        return "".join(out)
