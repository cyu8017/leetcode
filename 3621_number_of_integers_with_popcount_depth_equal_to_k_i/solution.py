# LeetCode 3621 - Number of Integers With Popcount Depth Equal to K I
# https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/


class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1 if n >= 1 else 0

        def bit_count(x: int) -> int:
            c = 0
            while x:
                c += x & 1
                x >>= 1
            return c

        def depth(x: int) -> int:
            if x <= 0:
                return 100
            d = 0
            while x > 1:
                x = bit_count(x)
                d += 1
            return d

        bits = []
        x = n
        while x > 0:
            bits.append(str(x & 1))
            x //= 2
        s = "".join(reversed(bits)) if bits else "0"
        memo = {}

        def dfs(pos: int, tight: int, started: int, pc: int) -> int:
            if pos == len(s):
                if started == 0:
                    return 0
                if pc == 1:
                    return 1 if k == 1 else 0
                return 1 if depth(pc) == k - 1 else 0
            key = (pos, tight, started, pc)
            if key in memo:
                return memo[key]
            up = int(s[pos]) if tight == 1 else 1
            res = 0
            for dig in range(up + 1):
                nt = 1 if tight == 1 and dig == up else 0
                if started == 0 and dig == 0:
                    res += dfs(pos + 1, nt, 0, 0)
                else:
                    res += dfs(pos + 1, nt, 1, pc + dig)
            memo[key] = res
            return res

        return dfs(0, 1, 0, 0)
