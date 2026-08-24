# LeetCode 2800 - Shortest String That Contains Three Strings
# https://leetcode.com/problems/shortest-string-that-contains-three-strings/


class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def merge(x: str, y: str) -> str:
            if y in x:
                return x
            best = x + y
            n = min(len(x), len(y))
            for i in range(n, 0, -1):
                if x[-i:] == y[:i]:
                    cand = x + y[i:]
                    if len(cand) < len(best) or (len(cand) == len(best) and cand < best):
                        best = cand
                    break
            return best

        perms = [
            [a, b, c],
            [a, c, b],
            [b, a, c],
            [b, c, a],
            [c, a, b],
            [c, b, a],
        ]
        ans = ""
        for p in perms:
            cur = merge(merge(p[0], p[1]), p[2])
            if not ans or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                ans = cur
        return ans
