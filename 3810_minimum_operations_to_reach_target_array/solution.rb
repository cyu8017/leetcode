# LeetCode 3810 - Minimum Operations to Reach Target Array
# https://leetcode.com/problems/minimum-operations-to-reach-target-array/

# @param {Integer[]} nums
# @param {Integer[]} target
# @return {Integer}
def min_operations(nums, target)
  s = {}
  (0...nums.length).each { |i| s[nums[i]] = true if nums[i] != target[i] }
  s.length
end
