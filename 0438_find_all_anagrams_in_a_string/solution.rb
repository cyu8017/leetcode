# LeetCode 0438 - Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution
  def find_anagrams(s, p)
    return [] if p.length > s.length

    need = Array.new(26, 0)
    window = Array.new(26, 0)
    p.each_char { |char| need[char.ord - "a".ord] += 1 }

    result = []
    left = 0
    s.each_char.with_index do |char, right|
      window[char.ord - "a".ord] += 1
      if right - left + 1 > p.length
        window[s[left].ord - "a".ord] -= 1
        left += 1
      end
      result << left if window == need
    end
    result
  end

  alias_method :findAnagrams, :find_anagrams
end
