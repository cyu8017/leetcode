# LeetCode 1877 - Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

# @param {Integer[]} nums
# @return {Integer}
def min_pair_sum(nums)
  nums = nums.sort
  (0...nums.length / 2).map { |i| nums[i] + nums[-1 - i] }.max
end
