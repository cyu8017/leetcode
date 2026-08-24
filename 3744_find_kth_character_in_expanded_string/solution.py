# LeetCode 3744 - Find Kth Character in Expanded String
# https://leetcode.com/problems/find-kth-character-in-expanded-string/

class Solution:
    def kthCharacter(self, s: str, k: int) -> str:
        words = s.strip().split()
        for w in words:
            m = (1 + len(w)) * len(w) // 2
            if k == m:
                return " "
            if k > m:
                k -= m + 1
            else:
                cur = 0
                i = 0
                while True:
                    cur += i + 1
                    if k < cur:
                        return w[i]
                    i += 1
        return " "
