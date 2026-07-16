# LeetCode 0395 - Longest Substring with At Least K Repeating Characters
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

class Solution
  def longest_substring(s, k)
    return 0 if s.empty?

    counts = Hash.new(0)
    s.each_char { |char| counts[char] += 1 }

    counts.each do |char, count|
      if count < k
        return s.split(char).map { |part| longest_substring(part, k) }.max
      end
    end

    s.length
  end

  alias_method :longestSubstring, :longest_substring
end
