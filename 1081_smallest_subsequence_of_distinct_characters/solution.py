# LeetCode 1081 - Smallest Subsequence of Distinct Characters
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}
        stack: list[str] = []
        used: set[str] = set()
        for i, ch in enumerate(s):
            if ch in used:
                continue
            while stack and ch < stack[-1] and last[stack[-1]] > i:
                used.remove(stack.pop())
            stack.append(ch)
            used.add(ch)
        return "".join(stack)
