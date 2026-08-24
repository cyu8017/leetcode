# LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K
# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  ans = 0
  nums.each { |x| ans = (ans + x) % k }
  ans
end
