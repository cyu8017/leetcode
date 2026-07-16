class Solution:
    def minChanges(self, nums, k):
        from collections import Counter
        freq = [Counter() for _ in range(k)]
        size = [0] * k
        for i, x in enumerate(nums):
            freq[i % k][x] += 1
            size[i % k] += 1
        dp = {0: 0}
        for i in range(k):
            ndp = {}
            for xv in range(256):
                cost = size[i] - freq[i].get(xv, 0)
                for xo, changes in dp.items():
                    key = xo ^ xv
                    ndp[key] = min(ndp.get(key, 10**9), changes + cost)
            dp = ndp
        return dp[0]
