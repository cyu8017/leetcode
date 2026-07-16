# LeetCode 0387 - First Unique Character in a String
# https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution
  def first_uniq_char(s)
    counts = Hash.new(0)
    s.each_char { |char| counts[char] += 1 }

    s.each_char.with_index do |char, index|
      return index if counts[char] == 1
    end

    -1
  end

  alias_method :firstUniqChar, :first_uniq_char
end
