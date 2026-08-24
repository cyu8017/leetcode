# LeetCode 3145 - Find Products of Elements of Big Array
# https://leetcode.com/problems/find-products-of-elements-of-big-array/

from typing import List


class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        M = 50
        cnt = [0] * (M + 1)
        s = [0] * (M + 1)
        p = 1
        for i in range(1, M + 1):
            cnt[i] = cnt[i - 1] * 2 + p
            s[i] = s[i - 1] * 2 + p * (i - 1)
            p *= 2

        def num_idx_and_sum(x: int):
            idx = 0
            total_sum = 0
            while x > 0:
                i = 0
                t = x
                while t > 1:
                    t >>= 1
                    i += 1
                idx += cnt[i]
                total_sum += s[i]
                x -= 1 << i
                total_sum += (x + 1) * i
                idx += x + 1
            return idx, total_sum

        def f(i: int) -> int:
            l = 0
            r = 1 << M
            while l < r:
                mid = (l + r + 1) >> 1
                p0 = num_idx_and_sum(mid)
                if p0[0] < i:
                    l = mid
                else:
                    r = mid - 1
            p0 = num_idx_and_sum(l)
            total_sum = p0[1]
            i -= p0[0]
            x = l + 1
            for _ in range(i):
                y = x & -x
                tz = 0
                yy = y
                while (yy & 1) == 0:
                    tz += 1
                    yy >>= 1
                total_sum += tz
                x -= y
            return total_sum

        def qpow(a: int, n: int, mod: int) -> int:
            ans = 1 % mod
            a %= mod
            while n > 0:
                if (n & 1) != 0:
                    ans = ans * a % mod
                a = a * a % mod
                n >>= 1
            return ans

        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            left, right, mod = q[0], q[1], q[2]
            power = f(right + 1) - f(left)
            ans[i] = qpow(2, power, mod)
        return ans
