# LeetCode 2014 - Longest Subsequence Repeated k Times
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

from collections import deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - 97] += 1
        chars = "".join(chr(97 + c) for c in range(25, -1, -1) if freq[c] >= k)

        def is_subseq(t: str) -> bool:
            need = 0
            times = 0
            for ch in s:
                if ch == t[need]:
                    need += 1
                    if need == len(t):
                        times += 1
                        if times == k:
                            return True
                        need = 0
            return False

        best = ""
        q = deque([""])
        while q:
            cur = q.popleft()
            for ch in chars:
                nxt = cur + ch
                if is_subseq(nxt):
                    if len(nxt) > len(best) or (len(nxt) == len(best) and nxt > best):
                        best = nxt
                    q.append(nxt)
        return best
