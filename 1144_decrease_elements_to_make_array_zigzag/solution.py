# LeetCode 1144 - Decrease Elements To Make Array Zigzag
# https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

class Solution:
    def movesToMakeZigzag(self, nums: list[int]) -> int:
        def cost(start: int) -> int:
            ans = 0
            for i in range(start, len(nums), 2):
                left = nums[i - 1] if i else float("inf")
                right = nums[i + 1] if i + 1 < len(nums) else float("inf")
                ans += max(0, nums[i] - min(left, right) + 1)
            return ans

        return min(cost(0), cost(1))
