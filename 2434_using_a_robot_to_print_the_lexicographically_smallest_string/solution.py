# LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        min_suf = [""] * (n + 1)
        min_suf[n] = chr(ord("z") + 1)
        for i in range(n - 1, -1, -1):
            min_suf[i] = s[i] if s[i] < min_suf[i + 1] else min_suf[i + 1]
        stack = []
        ans = []
        for i in range(n):
            stack.append(s[i])
            while stack and stack[-1] <= min_suf[i + 1]:
                ans.append(stack.pop())
        while stack:
            ans.append(stack.pop())
        return "".join(ans)
