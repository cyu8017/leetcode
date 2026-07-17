# LeetCode 1746 - Maximum Subarray Sum After One Operation
# https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

# @param {Integer[]} nums
# @return {Integer}
def max_sum_after_operation(nums)
  no_square = 0
  one_square = 0
  best = -(10**18)
  nums.each do |value|
    one_square = [one_square + value, no_square + value * value, value * value].max
    no_square = [no_square + value, value].max
    best = [best, one_square].max
  end
  best
end
