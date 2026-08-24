# LeetCode 3727 - Maximum Alternating Sum of Squares
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

# @param {Integer[]} nums
# @return {Integer}
def max_alternating_sum(nums)
  a = nums.map { |x| x * x }.sort
  m = a.length / 2
  ans = 0
  (0...m).each { |i| ans -= a[i] }
  (m...a.length).each { |i| ans += a[i] }
  ans
end
