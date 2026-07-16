# LeetCode 0344 - Reverse String
# https://leetcode.com/problems/reverse-string/

class Solution
  def reverse_string(s)
    left = 0
    right = s.length - 1
    while left < right
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
    end
  end

  alias_method :reverseString, :reverse_string
end
