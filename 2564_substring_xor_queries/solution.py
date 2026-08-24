# LeetCode 2564 - Substring XOR Queries
# https://leetcode.com/problems/substring-xor-queries/

from typing import List


class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        pos = {}
        n = len(s)
        for i in range(n):
            if s[i] == "0":
                if 0 not in pos:
                    pos[0] = [i, i]
                continue
            val = 0
            for j in range(i, min(n, i + 30)):
                val = val * 2 + (ord(s[j]) - 48)
                if val not in pos:
                    pos[val] = [i, j]
        ans = [None] * len(queries)
        for i, (a, b) in enumerate(queries):
            need = a ^ b
            ans[i] = pos[need][:] if need in pos else [-1, -1]
        return ans
