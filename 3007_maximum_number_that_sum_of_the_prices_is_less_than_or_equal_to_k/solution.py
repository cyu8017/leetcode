# LeetCode 3007 - Maximum Number That Sum of the Prices Is Less Than or Equal to K
# https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/


class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        num = 0
        f = []

        def dfs(pos: int, cnt: int, limit: bool) -> int:
            if pos == 0:
                return cnt
            if not limit and f[pos][cnt] != -1:
                return f[pos][cnt]
            ans = 0
            up = (num >> (pos - 1)) & 1 if limit else 1
            for i in range(up + 1):
                v = cnt
                if i == 1 and pos % x == 0:
                    v += 1
                ans += dfs(pos - 1, v, limit and i == up)
            if not limit:
                f[pos][cnt] = ans
            return ans

        l = 1
        r = 10 ** 17
        while l < r:
            mid = (l + r + 1) >> 1
            num = mid
            m = 0
            t = num
            while t > 0:
                m += 1
                t >>= 1
            f = [[-1] * 65 for _ in range(65)]
            if dfs(m, 0, True) <= k:
                l = mid
            else:
                r = mid - 1
        return l
