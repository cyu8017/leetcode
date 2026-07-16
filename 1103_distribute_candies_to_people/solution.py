# LeetCode 1103 - Distribute Candies to People
# https://leetcode.com/problems/distribute-candies-to-people/

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = [0] * num_people
        give = 1
        i = 0
        while candies:
            take = min(give, candies)
            ans[i] += take
            candies -= take
            give += 1
            i = (i + 1) % num_people
        return ans
