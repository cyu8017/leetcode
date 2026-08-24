# LeetCode 2344 - Minimum Deletions to Make Array Divisible
# https://leetcode.com/problems/minimum-deletions-to-make-array-divisible/

# @param {Integer[]} nums
# @param {Integer[]} nums_divide
# @return {Integer}
def min_operations(nums, nums_divide)
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  g = nums_divide[0]
  (1...nums_divide.length).each { |i| g = gcd.call(g, nums_divide[i]) }
  nums = nums.sort
  nums.each_with_index { |x, i| return i if g % x == 0 }
  -1
end
