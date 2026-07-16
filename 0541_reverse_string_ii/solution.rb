# LeetCode 0541 - Reverse String II
# https://leetcode.com/problems/reverse-string-ii/

class Solution
  def reverse_str(s, k)
    chars = s.chars
    start = 0
    while start < chars.length
      left = start
      right = [start + k, chars.length].min - 1
      while left < right
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
      end
      start += 2 * k
    end
    chars.join
  end

  alias_method :reverseStr, :reverse_str
end
