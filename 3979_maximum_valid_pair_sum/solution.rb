# LeetCode 3979 - Maximum Valid Pair Sum
# https://leetcode.com/problems/maximum-valid-pair-sum/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_valid_pair_sum(nums, k)
  ans = 0
  x = 0
  (k...nums.length).each do |j|
    y = nums[j]
    x = nums[j - k] if nums[j - k] > x
    ans = x + y if x + y > ans
  end
  ans
end
