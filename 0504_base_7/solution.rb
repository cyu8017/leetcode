# LeetCode 0504 - Base 7
# https://leetcode.com/problems/base-7/

class Solution
  def convert_to_base7(num)
    return "0" if num.zero?

    negative = num.negative?
    num = num.abs
    digits = []
    while num.positive?
      digits << (num % 7).to_s
      num /= 7
    end
    result = digits.reverse.join
    negative ? "-#{result}" : result
  end

  alias_method :convertToBase7, :convert_to_base7
end
