# LeetCode 0424 - Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution
  def character_replacement(s, k)
    counts = Hash.new(0)
    left = 0
    best = 0
    max_count = 0

    s.each_char.with_index do |char, right|
      counts[char] += 1
      max_count = [max_count, counts[char]].max
      while (right - left + 1) - max_count > k
        counts[s[left]] -= 1
        left += 1
      end
      best = [best, right - left + 1].max
    end

    best
  end

  alias_method :characterReplacement, :character_replacement
end
