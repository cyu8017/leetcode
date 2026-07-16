# LeetCode 0394 - Decode String
# https://leetcode.com/problems/decode-string/

class Solution
  def decode_string(s)
    stack = []
    current = ""
    number = 0

    s.each_char do |char|
      if char >= "0" && char <= "9"
        number = number * 10 + char.to_i
      elsif char == "["
        stack << [current, number]
        current = ""
        number = 0
      elsif char == "]"
        previous, count = stack.pop
        current = previous + current * count
      else
        current += char
      end
    end

    current
  end

  alias_method :decodeString, :decode_string
end
