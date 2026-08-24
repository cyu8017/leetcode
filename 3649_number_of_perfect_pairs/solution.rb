# LeetCode 3649 - Number of Perfect Pairs
# https://leetcode.com/problems/number-of-perfect-pairs/

# @param {Integer[]} nums
# @return {Integer}
def perfect_pairs(nums)
  n = nums.length
  abs_nums = nums.map(&:abs).sort
  ans = 0
  j = 0
  (0...n).each do |i|
    j = i + 1 if j < i + 1
    j += 1 while j < n && abs_nums[j] <= 2 * abs_nums[i]
    ans += j - i - 1
  end
  ans
end
