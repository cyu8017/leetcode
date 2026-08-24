# LeetCode 3982 - Sum of Integers with Maximum Digit Range
# https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

# @param {Integer[]} nums
# @return {Integer}
def max_digit_range(nums)
  mx = 0
  ans = 0
  nums.each do |x|
    a = 10
    b = 0
    y = x
    while y > 0
      v = y % 10
      a = v if v < a
      b = v if v > b
      y /= 10
    end
    r = b - a
    if mx < r
      mx = r
      ans = x
    elsif mx == r
      ans += x
    end
  end
  ans
end
