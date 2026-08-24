# LeetCode 3170 - Lexicographically Minimum String After Removing Stars
# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/


class Solution:
    def clearStars(self, s: str) -> str:
        g = [[] for _ in range(26)]
        n = len(s)
        rem = [False] * n
        for i, ch in enumerate(s):
            if ch == "*":
                rem[i] = True
                for j in range(26):
                    if g[j]:
                        rem[g[j].pop()] = True
                        break
            else:
                g[ord(ch) - 97].append(i)
        return "".join(s[i] for i in range(n) if not rem[i])
