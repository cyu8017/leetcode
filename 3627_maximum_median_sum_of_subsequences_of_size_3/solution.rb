# LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

# @param {Integer[]} nums
# @return {Integer}
def maximum_median_sum(nums)
  nums = nums.sort
  n = nums.length
  ans = 0
  (n / 3...n).step(2) { |i| ans += nums[i] }
  ans
end
