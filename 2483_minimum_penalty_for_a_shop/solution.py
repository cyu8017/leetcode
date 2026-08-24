# LeetCode 2483 - Minimum Penalty for a Shop
# https://leetcode.com/problems/minimum-penalty-for-a-shop/


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        penalty = 0
        for c in customers:
            if c == "Y":
                penalty += 1
        best = penalty
        ans = 0
        for i in range(n):
            if customers[i] == "Y":
                penalty -= 1
            else:
                penalty += 1
            if penalty < best:
                best = penalty
                ans = i + 1
        return ans
