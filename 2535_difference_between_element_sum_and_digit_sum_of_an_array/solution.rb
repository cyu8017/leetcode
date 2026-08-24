# LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

# @param {Integer[]} nums
# @return {Integer}
def difference_of_sum(nums)
  elem = 0
  digit = 0
  nums.each do |num|
    elem += num
    x = num
    while x > 0
      digit += x % 10
      x /= 10
    end
  end
  (elem - digit).abs
end
