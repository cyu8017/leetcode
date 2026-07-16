# LeetCode 0224 - Basic Calculator
# https://leetcode.com/problems/basic-calculator/

# @param {String} s
# @return {Integer}
def calculate(s)
  stack = []
  result = 0
  number = 0
  sign = 1
  s.each_char do |char|
    if char >= "0" && char <= "9"
      number = number * 10 + char.ord - 48
    elsif char == "+" || char == "-"
      result += sign * number
      number = 0
      sign = char == "+" ? 1 : -1
    elsif char == "("
      stack.push(result)
      stack.push(sign)
      result = 0
      sign = 1
    elsif char == ")"
      result += sign * number
      number = 0
      result *= stack.pop
      result += stack.pop
    end
  end
  result + sign * number
end
