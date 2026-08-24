# LeetCode 3747 - Count Distinct Integers After Removing Zeros
# https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

class Solution:
    def countDistinct(self, n: int) -> int:
        s = str(n)
        m = len(s)
        f = [[[[-1] * 2 for _ in range(2)] for _ in range(2)] for _ in range(20)]

        def dfs(i: int, zero: int, lead: int, limit: int) -> int:
            if i == m:
                return 1 if zero == 0 and lead == 0 else 0
            if limit == 0 and f[i][zero][lead][limit] != -1:
                return f[i][zero][lead][limit]
            up = ord(s[i]) - 48 if limit == 1 else 9
            ans = 0
            for d in range(up + 1):
                nxt_zero = zero
                if d == 0 and lead == 0:
                    nxt_zero = 1
                nxt_lead = 1 if lead == 1 and d == 0 else 0
                nxt_limit = 1 if limit == 1 and d == up else 0
                ans += dfs(i + 1, nxt_zero, nxt_lead, nxt_limit)
            if limit == 0:
                f[i][zero][lead][limit] = ans
            return ans

        return dfs(0, 0, 1, 1)
