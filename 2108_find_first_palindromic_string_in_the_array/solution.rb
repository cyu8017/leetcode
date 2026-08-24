# LeetCode 2108 - Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

# @param {String[]} words
# @return {String}
def first_palindrome(words)
  words.each { |w| return w if w == w.reverse }
  ""
end
