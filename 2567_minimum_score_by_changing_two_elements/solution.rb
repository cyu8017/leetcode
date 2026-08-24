# LeetCode 2567 - Minimum Score by Changing Two Elements
# https://leetcode.com/problems/minimum-score-by-changing-two-elements/

# @param {Integer[]} nums
# @return {Integer}
def minimize_sum(nums)
  nums = nums.sort
  n = nums.length
  [nums[n - 1] - nums[2], nums[n - 3] - nums[0], nums[n - 2] - nums[1]].min
end
