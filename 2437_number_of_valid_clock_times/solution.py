# LeetCode 2437 - Number of Valid Clock Times
# https://leetcode.com/problems/number-of-valid-clock-times/


class Solution:
    def countTime(self, time: str) -> int:
        ans = 0
        for h in range(24):
            for m in range(60):
                h0, h1 = str(h // 10), str(h % 10)
                m0, m1 = str(m // 10), str(m % 10)
                if time[0] != "?" and time[0] != h0:
                    continue
                if time[1] != "?" and time[1] != h1:
                    continue
                if time[3] != "?" and time[3] != m0:
                    continue
                if time[4] != "?" and time[4] != m1:
                    continue
                ans += 1
        return ans
