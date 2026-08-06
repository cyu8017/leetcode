# LeetCode 1413 - Minimum Value To Get Positive Step By Step Sum
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

def min_start_value(nums)
  prefix = lowest = 0
  nums.each do |value|
    prefix += value
    lowest = [lowest, prefix].min
  end
  1 - lowest
end
