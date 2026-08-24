# LeetCode 2180 - Count Integers With Even Digit Sum
# https://leetcode.com/problems/count-integers-with-even-digit-sum/

# @param {Integer} num
# @return {Integer}
def count_even(num)
  ans = 0
  (1..num).each do |x|
    s = 0
    y = x
    while y > 0
      s += y % 10
      y /= 10
    end
    ans += 1 if s.even?
  end
  ans
end
