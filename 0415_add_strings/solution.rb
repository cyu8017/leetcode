# LeetCode 0415 - Add Strings
# https://leetcode.com/problems/add-strings/

class Solution
  def add_strings(num1, num2)
    index1 = num1.length - 1
    index2 = num2.length - 1
    carry = 0
    digits = []

    while index1 >= 0 || index2 >= 0 || carry.positive?
      if index1 >= 0
        carry += num1[index1].to_i
        index1 -= 1
      end
      if index2 >= 0
        carry += num2[index2].to_i
        index2 -= 1
      end
      digits << (carry % 10).to_s
      carry /= 10
    end

    digits.reverse.join
  end

  alias_method :addStrings, :add_strings
end
