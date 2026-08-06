# LeetCode 1332 - Remove Palindromic Subsequences
# https://leetcode.com/problems/remove-palindromic-subsequences/

def remove_palindrome_sub(s)
  return 0 if s.empty?
  s == s.reverse ? 1 : 2
end
