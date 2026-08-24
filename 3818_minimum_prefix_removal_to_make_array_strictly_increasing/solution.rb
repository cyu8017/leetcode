# LeetCode 3818 - Minimum Prefix Removal to Make Array Strictly Increasing
# https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

# @param {Integer[]} nums
# @return {Integer}
def minimum_prefix_length(nums)
  (nums.length - 1).downto(1) { |i| return i if nums[i - 1] >= nums[i] }
  0
end
