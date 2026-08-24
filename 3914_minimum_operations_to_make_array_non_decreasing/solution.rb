# LeetCode 3914 - Minimum Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  (1...nums.length).each { |i| ans += [0, nums[i - 1] - nums[i]].max }
  ans
end
