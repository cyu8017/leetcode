# LeetCode 2697 - Lexicographically Smallest Palindrome
# https://leetcode.com/problems/lexicographically-smallest-palindrome/

# @param {String} s
# @return {String}
def make_smallest_palindrome(s)
  arr = s.chars
  n = arr.length
  (n / 2).times do |i|
    c = arr[i] < arr[n - 1 - i] ? arr[i] : arr[n - 1 - i]
    arr[i] = arr[n - 1 - i] = c
  end
  arr.join
end
