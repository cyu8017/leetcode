# LeetCode 1749 - Maximum Absolute Sum of Any Subarray
# https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

# @param {Integer[]} nums
# @return {Integer}
def max_absolute_sum(nums)
  prefix = 0
  low = 0
  high = 0
  nums.each do |value|
    prefix += value
    low = prefix if prefix < low
    high = prefix if prefix > high
  end
  high - low
end
