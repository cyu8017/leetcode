# LeetCode 0005 - Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

# @param {String} s
# @return {String}
def longest_palindrome(s)
  best_start = 0
  best_len = 0

  expand = lambda do |left, right|
    while left >= 0 && right < s.length && s[left] == s[right]
      left -= 1
      right += 1
    end
    len = right - left - 1
    if len > best_len
      best_len = len
      best_start = left + 1
    end
  end

  (0...s.length).each do |i|
    expand.call(i, i)
    expand.call(i, i + 1)
  end

  s[best_start, best_len]
end
