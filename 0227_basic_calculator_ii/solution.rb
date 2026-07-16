# LeetCode 0227 - Basic Calculator II
# https://leetcode.com/problems/basic-calculator-ii/

# @param {String} s
# @return {Integer}
def calculate(s)
  stack = []
  number = 0
  operator = "+"

  s.each_char.with_index do |char, index|
    if char >= "0" && char <= "9"
      number = number * 10 + char.ord - 48
    end
    if "+-*/".include?(char) || index == s.length - 1
      case operator
      when "+"
        stack << number
      when "-"
        stack << -number
      when "*"
        stack[-1] = stack.pop * number
      when "/"
        stack[-1] = (stack.pop.to_f / number).truncate.to_i
      end
      operator = char
      number = 0
    end
  end

  stack.sum
end
