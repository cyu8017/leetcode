# LeetCode 3723 - Maximize Sum of Squares of Digits
# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

# @param {Integer} num
# @param {Integer} sum
# @return {String}
def max_sum_of_squares(num, sum)
  return "" if num * 9 < sum
  k, rem = sum.divmod(9)
  ans = "9" * k
  ans += (48 + rem).chr if rem > 0
  ans += "0" while ans.length < num
  ans
end
