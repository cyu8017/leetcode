# LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
# https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/


class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        road = road + "."
        n = len(road)
        cnt = [0] * n
        k = 0
        ans = 0
        for c in road:
            if c == "x":
                k += 1
            elif k > 0:
                cnt[k] += 1
                k = 0
        k = n - 1
        while k > 0 and budget > 0:
            t = min(budget // (k + 1), cnt[k])
            ans += t * k
            budget -= t * (k + 1)
            cnt[k - 1] += cnt[k] - t
            k -= 1
        return ans
