# LeetCode 3455 - Shortest Matching Substring
# https://leetcode.com/problems/shortest-matching-substring/

from typing import List


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        parts: List[str] = []
        cur = ""
        for c in p:
            if c == "*":
                parts.append(cur)
                cur = ""
            else:
                cur += c
        parts.append(cur)
        while len(parts) < 3:
            parts.append("")
        a, b, c = parts[0], parts[1], parts[2]
        n = len(s)

        def find_all(sub: str) -> List[int]:
            res = []
            if len(sub) == 0:
                for i in range(n + 1):
                    res.append(i)
                return res
            for i in range(n - len(sub) + 1):
                if s.startswith(sub, i):
                    res.append(i)
            return res

        def sort_search(arr: List[int], x: int) -> int:
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) >> 1
                if arr[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        pos_a, pos_b, pos_c = find_all(a), find_all(b), find_all(c)
        ans = n + 1
        for ia in pos_a:
            end_a = ia + len(a)
            bi = sort_search(pos_b, end_a)
            while bi < len(pos_b):
                end_b = pos_b[bi] + len(b)
                ci = sort_search(pos_c, end_b)
                if ci < len(pos_c):
                    length = pos_c[ci] + len(c) - ia
                    if length < ans:
                        ans = length
                break
        return -1 if ans == n + 1 else ans
