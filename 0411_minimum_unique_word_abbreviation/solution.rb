# LeetCode 0411 - Minimum Unique Word Abbreviation
# https://leetcode.com/problems/minimum-unique-word-abbreviation/

class Solution
  def min_abbreviation(target, dictionary)
    @target = target
    @words = dictionary.select { |word| word.length == target.length }
    @best_len = target.length + 1
    @result = target
    dfs(0, [], 0)
    @result
  end

  alias_method :minAbbreviation, :min_abbreviation

  private

  def matches?(word, abbr)
    index = 0
    pointer = 0
    while index < word.length && pointer < abbr.length
      if abbr[pointer].match?(/\d/)
        return false if abbr[pointer] == "0"

        number = 0
        while pointer < abbr.length && abbr[pointer].match?(/\d/)
          number = number * 10 + abbr[pointer].to_i
          pointer += 1
        end
        index += number
      else
        return false if word[index] != abbr[pointer]

        index += 1
        pointer += 1
      end
    end
    index == word.length && pointer == abbr.length
  end

  def valid?(abbr)
    return false unless matches?(@target, abbr)

    @words.none? { |word| matches?(word, abbr) }
  end

  def dfs(index, parts, skip)
    if index == @target.length
      abbr = parts.join + (skip.positive? ? skip.to_s : "")
      if valid?(abbr) && (abbr.length < @best_len || (abbr.length == @best_len && abbr < @result))
        @best_len = abbr.length
        @result = abbr
      end
      return
    end

    dfs(index + 1, parts, skip + 1)

    new_parts = parts.dup
    new_parts << skip.to_s if skip.positive?
    new_parts << @target[index]
    dfs(index + 1, new_parts, 0)
  end
end
