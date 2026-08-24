# LeetCode 3490 - Count Beautiful Numbers
# https://leetcode.com/problems/count-beautiful-numbers/


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def count_beautiful(n: int) -> int:
            if n <= 0:
                return 0
            s = str(n)

            def dfs(pos: int, tight: bool, sm: int, prod: int, started: bool) -> int:
                if pos == len(s):
                    if not started:
                        return 0
                    return 1 if sm > 0 and prod % sm == 0 else 0
                up = ord(s[pos]) - 48 if tight else 9
                ans = 0
                for d in range(up + 1):
                    nt = tight and d == up
                    if not started and d == 0:
                        ans += dfs(pos + 1, nt, 0, 1, False)
                    else:
                        ns = sm + d
                        np = d if not started else prod * d
                        ans += dfs(pos + 1, nt, ns, np, True)
                return ans

            return dfs(0, True, 0, 1, False)

        return count_beautiful(r) - count_beautiful(l - 1)
