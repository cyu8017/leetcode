# LeetCode 2147 - Number of Ways to Divide a Long Corridor
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1000000007
        seats = []
        for i in range(len(corridor)):
            if corridor[i] == "S":
                seats.append(i)
        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0
        ans = 1
        for i in range(2, len(seats), 2):
            ans = ans * (seats[i] - seats[i - 1]) % MOD
        return ans
