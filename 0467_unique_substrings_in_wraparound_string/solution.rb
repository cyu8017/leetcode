# LeetCode 0467 - Unique Substrings in Wraparound String
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/

class Solution
  def find_substring_in_wrapround_string(s)
    counts = Array.new(26, 0)
    length = 0

    s.each_char.with_index do |char, index|
      if index.positive? && (char.ord - s[index - 1].ord + 26) % 26 == 1
        length += 1
      else
        length = 1
      end
      position = char.ord - "a".ord
      counts[position] = [counts[position], length].max
    end

    counts.sum
  end

  alias_method :findSubstringInWraproundString, :find_substring_in_wrapround_string
end
