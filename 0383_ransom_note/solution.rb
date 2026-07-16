# LeetCode 0383 - Ransom Note
# https://leetcode.com/problems/ransom-note/

class Solution
  def can_construct(ransom_note, magazine)
    counts = Hash.new(0)
    magazine.each_char { |char| counts[char] += 1 }

    ransom_note.each_char do |char|
      return false if counts[char] == 0
      counts[char] -= 1
    end

    true
  end

  alias_method :canConstruct, :can_construct
end
