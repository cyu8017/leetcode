# LeetCode 2778 - Sum of Squares of Special Elements
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

# @param {Integer[]} nums
# @return {Integer}
def sum_of_squares(nums)
  n = nums.length
  ans = 0
  (0...n).each { |i| ans += nums[i] * nums[i] if n % (i + 1) == 0 }
  ans
end
