# LeetCode 3032 - Count Numbers With Unique Digits II
# https://leetcode.com/problems/count-numbers-with-unique-digits-ii/


class Solution:
    def numberCount(self, a: int, b: int) -> int:
        num = ""
        f = []

        def reset() -> None:
            nonlocal f
            f = [[-1] * (1 << 10) for _ in range(len(num))]

        def dfs(pos: int, mask: int, limit: bool) -> int:
            if pos >= len(num):
                return 1 if mask != 0 else 0
            if not limit and f[pos][mask] != -1:
                return f[pos][mask]
            up = ord(num[pos]) - 48 if limit else 9
            ans = 0
            for i in range(up + 1):
                if ((mask >> i) & 1) != 0:
                    continue
                nxt = mask | (1 << i)
                if mask == 0 and i == 0:
                    nxt = 0
                ans += dfs(pos + 1, nxt, limit and i == up)
            if not limit:
                f[pos][mask] = ans
            return ans

        num = str(b)
        reset()
        y = dfs(0, 0, True)
        num = str(a - 1)
        reset()
        x = dfs(0, 0, True)
        return y - x
