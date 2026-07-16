# LeetCode 0527 - Word Abbreviation
# https://leetcode.com/problems/word-abbreviation/

class Solution
  def words_abbreviation(words)
    prefixes = Array.new(words.length, 1)
    changed = true
    while changed
      changed = false
      groups = Hash.new { |hash, key| hash[key] = [] }
      words.each_with_index do |word, index|
        groups[abbreviate(word, prefixes[index])] << index
      end
      groups.each_value do |indices|
        next unless indices.length > 1

        changed = true
        indices.each { |index| prefixes[index] += 1 }
      end
    end
    words.each_with_index.map { |word, index| abbreviate(word, prefixes[index]) }
  end

  alias_method :wordsAbbreviation, :words_abbreviation

  private

  def abbreviate(word, prefix)
    return word if prefix + 2 >= word.length

    middle = word.length - prefix - 1
    candidate = "#{word[0, prefix]}#{middle}#{word[-1]}"
    candidate.length < word.length ? candidate : word
  end
end
