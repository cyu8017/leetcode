# LeetCode 2086 - Minimum Number of Food Buckets to Feed the Hamsters
# https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/


class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        b = list(hamsters)
        ans = 0
        for i in range(len(b)):
            if b[i] != "H":
                continue
            if i > 0 and b[i - 1] == "B":
                continue
            if i + 1 < len(b) and b[i + 1] == ".":
                b[i + 1] = "B"
                ans += 1
            elif i > 0 and b[i - 1] == ".":
                b[i - 1] = "B"
                ans += 1
            else:
                return -1
        return ans
