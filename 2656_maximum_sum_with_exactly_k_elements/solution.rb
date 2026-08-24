# LeetCode 2656 - Maximum Sum With Exactly K Elements
# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def maximize_sum(nums, k)
  mx = nums[0]
  nums.each { |x| mx = x if x > mx }
  k * mx + k * (k - 1) / 2
end
