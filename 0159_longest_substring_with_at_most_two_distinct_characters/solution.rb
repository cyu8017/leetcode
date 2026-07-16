# LeetCode 0159 - Longest Substring with At Most Two Distinct Characters
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

class Solution
  def length_of_longest_substring_two_distinct(s)
    counts = Hash.new(0)
    left = 0
    best = 0
    characters = s.chars
    characters.each_with_index do |character, right|
      counts[character] += 1
      while counts.length > 2
        counts[characters[left]] -= 1
        counts.delete(characters[left]) if counts[characters[left]].zero?
        left += 1
      end
      best = [best, right - left + 1].max
    end
    best
  end
end