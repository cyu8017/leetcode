# LeetCode 0316 - Remove Duplicate Letters
# https://leetcode.com/problems/remove-duplicate-letters/

class Solution
  def removeDuplicateLetters(s)
    last_index = {}
    s.each_char.with_index { |char, index| last_index[char] = index }
    stack = []
    seen = {}
    s.each_char.with_index do |char, index|
      next if seen[char]

      while stack.any? && stack[-1] > char && last_index[stack[-1]] > index
        seen.delete(stack.pop)
      end
      stack << char
      seen[char] = true
    end
    stack.join
  end
end
