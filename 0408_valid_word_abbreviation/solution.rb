# LeetCode 0408 - Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/

class Solution
  def valid_word_abbreviation(word, abbr)
    i = 0
    j = 0
    while i < word.length && j < abbr.length
      if abbr[j] >= "0" && abbr[j] <= "9"
        return false if abbr[j] == "0"

        number = 0
        while j < abbr.length && abbr[j] >= "0" && abbr[j] <= "9"
          number = number * 10 + abbr[j].to_i
          j += 1
        end
        i += number
      else
        return false if word[i] != abbr[j]
        i += 1
        j += 1
      end
    end
    i == word.length && j == abbr.length
  end

  alias_method :validWordAbbreviation, :valid_word_abbreviation
end
