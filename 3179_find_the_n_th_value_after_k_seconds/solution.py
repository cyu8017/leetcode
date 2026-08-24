# LeetCode 3179 - Find the N-th Value After K Seconds
# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod = 1000000007
        a = [1] * n
        while k > 0:
            for i in range(1, n):
                a[i] = (a[i] + a[i - 1]) % mod
            k -= 1
        return a[n - 1]
