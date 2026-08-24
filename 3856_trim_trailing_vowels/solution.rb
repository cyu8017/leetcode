# LeetCode 3856 - Trim Trailing Vowels
# https://leetcode.com/problems/trim-trailing-vowels/

# @param {String} s
# @return {String}
def trim_trailing_vowels(s)
  i = s.length - 1
  i -= 1 while i >= 0 && "aeiou".include?(s[i])
  s[0, i + 1]
end
