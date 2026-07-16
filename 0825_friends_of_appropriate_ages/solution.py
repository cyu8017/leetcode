# LeetCode 0825 - Friends Of Appropriate Ages
# https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count = [0] * 121
        for age in ages:
            count[age] += 1
        ans = 0
        for x in range(1, 121):
            if count[x] == 0:
                continue
            for y in range(1, 121):
                if count[y] == 0:
                    continue
                if y <= 0.5 * x + 7 or y > x or (y > 100 and x < 100):
                    continue
                ans += count[x] * count[y]
                if x == y:
                    ans -= count[x]
        return ans
