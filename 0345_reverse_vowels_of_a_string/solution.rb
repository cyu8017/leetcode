# LeetCode 0345 - Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution
  def reverse_vowels(s)
    vowels = "aeiouAEIOU"
    chars = s.chars
    left = 0
    right = chars.length - 1

    while left < right
      left += 1 while left < right && !vowels.include?(chars[left])
      right -= 1 while left < right && !vowels.include?(chars[right])
      chars[left], chars[right] = chars[right], chars[left]
      left += 1
      right -= 1
    end

    chars.join
  end

  alias_method :reverseVowels, :reverse_vowels
end
