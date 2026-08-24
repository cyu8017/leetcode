# LeetCode 2330 - Valid Palindrome IV
# https://leetcode.com/problems/valid-palindrome-iv/

# @param {String} s
# @return {Boolean}
def make_palindrome(s)
  diff = 0
  i = 0
  j = s.length - 1
  while i < j
    if s[i] != s[j]
      diff += 1
      return false if diff > 2
    end
    i += 1
    j -= 1
  end
  true
end

alias solve make_palindrome
