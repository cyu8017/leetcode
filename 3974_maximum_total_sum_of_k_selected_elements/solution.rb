# LeetCode 3974 - Maximum Total Sum Of K Selected Elements
# https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} mul
# @return {Integer}
def max_sum(nums, k, mul)
  nums = nums.sort
  n = nums.length
  ans = 0
  (n - 1).downto(n - k) do |i|
    m = [1, mul].max
    ans += nums[i] * m
    mul -= 1
  end
  ans
end
