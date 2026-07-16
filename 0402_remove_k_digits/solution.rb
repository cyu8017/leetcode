# LeetCode 0402 - Remove K Digits
# https://leetcode.com/problems/remove-k-digits/

class Solution
  def remove_kdigits(num, k)
    stack = []
    num.each_char do |digit|
      while k > 0 && !stack.empty? && stack.last > digit
        stack.pop
        k -= 1
      end
      stack << digit
    end

    stack = stack[0...stack.length - k] if k > 0

    result = stack.join.sub(/\A0+/, "")
    result.empty? ? "0" : result
  end

  alias_method :removeKdigits, :remove_kdigits
end
