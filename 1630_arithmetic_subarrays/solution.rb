# LeetCode 1630 - Arithmetic Subarrays
# https://leetcode.com/problems/arithmetic-subarrays/

# @param {Integer[]} nums
# @param {Integer[]} l
# @param {Integer[]} r
# @return {Boolean[]}
def check_arithmetic_subarrays(nums, l, r)
  l.zip(r).map do |a, b|
    x = nums[a..b].sort
    x.length < 3 || (1...x.length).map { |i| x[i] - x[i - 1] }.uniq.length == 1
  end
end
