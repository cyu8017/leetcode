# LeetCode 1330 - Reverse Subarray To Maximize Array Value
# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

def max_value_after_reverse(nums)
  base = nums.each_cons(2).sum { |a, b| (a - b).abs }
  gain = 0
  low = 10**9
  high = -10**9
  nums.each_cons(2) do |a, b|
    gain = [gain, (nums[0] - b).abs - (a - b).abs, (nums[-1] - a).abs - (a - b).abs].max
    low = [low, [a, b].max].min
    high = [high, [a, b].min].max
  end
  base + [gain, 2 * (high - low)].max
end
