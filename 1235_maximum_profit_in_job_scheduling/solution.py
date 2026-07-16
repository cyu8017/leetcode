from bisect import bisect_right

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        ends, dp = [0], [0]
        for end, start, gain in jobs:
            i = bisect_right(ends, start) - 1
            ends.append(end)
            dp.append(max(dp[-1], dp[i] + gain))
        return dp[-1]
