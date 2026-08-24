# LeetCode 2162 - Minimum Cost to Set Cooking Time
# https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            if mins < 0 or mins > 99 or secs < 0 or secs > 99:
                return (2 ** 53 - 1) // 2
            s = None
            if mins > 0:
                s = str(mins) + str(secs // 10) + str(secs % 10)
            else:
                s = str(secs)
            cur = str(startAt)
            ans = 0
            for i in range(len(s)):
                c = s[i]
                if c != cur:
                    ans += moveCost
                    cur = c
                ans += pushCost
            return ans

        mins = targetSeconds // 60
        secs = targetSeconds % 60
        ans = cost(mins, secs)
        if mins > 0:
            ans = min(ans, cost(mins - 1, secs + 60))
        return ans
