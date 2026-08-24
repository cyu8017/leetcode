# LeetCode 3210 - Find the Encrypted String
# https://leetcode.com/problems/find-the-encrypted-string/

class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        out = []
        for i in range(n):
            out.append(s[(i + k) % n])
        return "".join(out)
