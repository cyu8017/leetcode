# LeetCode 2663 - Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/lexicographically-smallest-beautiful-string/


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        n = len(s)
        b = list(s)
        for i in range(n - 1, -1, -1):
            for code in range(ord(b[i]) + 1, 97 + k):
                c = chr(code)
                if (i > 0 and c == b[i - 1]) or (i > 1 and c == b[i - 2]):
                    continue
                b[i] = c
                for j in range(i + 1, n):
                    for nc in range(97, 97 + k):
                        ch = chr(nc)
                        if (j > 0 and ch == b[j - 1]) or (j > 1 and ch == b[j - 2]):
                            continue
                        b[j] = ch
                        break
                return "".join(b)
        return ""
