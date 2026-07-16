# LeetCode 0405 - Convert a Number to Hexadecimal
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution
  def to_hex(num)
    return "0" if num == 0

    digits = "0123456789abcdef"
    value = num & 0xFFFFFFFF
    result = []

    while value != 0
      result << digits[value & 15]
      value >>= 4
    end

    result.reverse.join
  end

  alias_method :toHex, :to_hex
end
