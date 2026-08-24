# LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)
        for i in range(n):
            ones = 0
            for j in range(i, n):
                if s[j] == "1":
                    ones += 1
                if ones == k:
                    cand = s[i : j + 1]
                    if not ans or len(cand) < len(ans) or (len(cand) == len(ans) and cand < ans):
                        ans = cand
                    break
                if ones > k:
                    break
        return ans
