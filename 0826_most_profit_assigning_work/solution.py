# LeetCode 0826 - Most Profit Assigning Work
# https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(
        self, difficulty: list[int], profit: list[int], worker: list[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = best = i = 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans
