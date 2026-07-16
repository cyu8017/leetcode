# LeetCode 0340 - Longest Substring with At Most K Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

class Solution
  def length_of_longest_substring_k_distinct(s, k)
    return 0 if k.zero?

    counts = Hash.new(0)
    left = 0
    best = 0

    s.each_char.with_index do |char, right|
      counts[char] += 1
      while counts.length > k
        left_char = s[left]
        counts[left_char] -= 1
        counts.delete(left_char) if counts[left_char].zero?
        left += 1
      end
      best = [best, right - left + 1].max
    end

    best
  end

  alias_method :lengthOfLongestSubstringKDistinct, :length_of_longest_substring_k_distinct
end
