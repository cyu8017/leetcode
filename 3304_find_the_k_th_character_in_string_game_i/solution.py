# LeetCode 3304 - Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            n = len(s)
            add = []
            for i in range(n):
                add.append(chr(97 + ((ord(s[i]) - 97 + 1) % 26)))
            s += "".join(add)
        return s[k - 1]
