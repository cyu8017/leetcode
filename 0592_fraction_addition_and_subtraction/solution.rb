# LeetCode 0592 - Fraction Addition and Subtraction
# https://leetcode.com/problems/fraction-addition-and-subtraction/

# @param {String} expression
# @return {String}
def fraction_addition(expression)
  nums = expression.scan(/[+-]?\d+/).map(&:to_i)
  numerator = 0
  denominator = 1

  (0...nums.length).step(2) do |i|
    a = nums[i]
    b = nums[i + 1]
    numerator = numerator * b + a * denominator
    denominator *= b
    g = numerator.gcd(denominator)
    numerator /= g
    denominator /= g
  end

  "#{numerator}/#{denominator}"
end
