# LeetCode 1558 - Minimum Numbers of Function Calls to Make Target Array
# https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  bit_count = nums.sum { |x| x.to_s(2).count('1') }
  max_len = nums.map { |x| x.bit_length - 1 }.max || 0
  bit_count + max_len
end
