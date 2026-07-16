# LeetCode 0409 - Longest Palindrome
# https://leetcode.com/problems/longest-palindrome/

class Solution
  def longest_palindrome(s)
    counts = Hash.new(0)
    s.each_char { |char| counts[char] += 1 }

    length = 0
    odd = false
    counts.each_value do |count|
      length += (count / 2) * 2
      odd = true if count.odd?
    end

    length + (odd ? 1 : 0)
  end

  alias_method :longestPalindrome, :longest_palindrome
end
