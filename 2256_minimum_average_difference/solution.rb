# LeetCode 2256 - Minimum Average Difference
# https://leetcode.com/problems/minimum-average-difference/

# @param {Integer[]} nums
# @return {Integer}
def minimum_average_difference(nums)
  n = nums.length
  total = nums.sum
  left = 0
  best_diff = Float::INFINITY
  best_idx = 0
  n.times do |i|
    left += nums[i]
    left_avg = left / (i + 1)
    right_avg = i == n - 1 ? 0 : (total - left) / (n - i - 1)
    diff = (left_avg - right_avg).abs
    if diff < best_diff
      best_diff = diff
      best_idx = i
    end
  end
  best_idx
end
