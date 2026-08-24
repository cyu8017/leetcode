# LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
# https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  n = nums.length
  ans = 10**18
  (0..(n - k)).each do |i|
    sub = nums[i, k].sort
    med = sub[k / 2]
    cost = 0
    sub.each { |x| cost += (x - med).abs }
    ans = cost if cost < ans
  end
  ans
end
