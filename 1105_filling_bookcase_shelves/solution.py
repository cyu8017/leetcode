# LeetCode 1105 - Filling Bookcase Shelves
# https://leetcode.com/problems/filling-bookcase-shelves/

class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            width = height = 0
            dp[i] = float("inf")
            for j in range(i, 0, -1):
                w, h = books[j - 1]
                width += w
                if width > shelfWidth:
                    break
                height = max(height, h)
                dp[i] = min(dp[i], dp[j - 1] + height)
        return dp[n]
