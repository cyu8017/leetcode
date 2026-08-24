# LeetCode 3663 - Find The Least Frequent Digit
# https://leetcode.com/problems/find-the-least-frequent-digit/


class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = [0] * 10
        ans = 0
        f = 1 << 30
        while n > 0:
            cnt[n % 10] += 1
            n //= 10
        for x in range(10):
            if cnt[x] > 0 and cnt[x] < f:
                f = cnt[x]
                ans = x
        return ans
