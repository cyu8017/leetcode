# LeetCode 0288 - Unique Word Abbreviation
# https://leetcode.com/problems/unique-word-abbreviation/

class ValidWordAbbr
  def initialize(dictionary)
    @groups = Hash.new { |hash, key| hash[key] = {} }
    dictionary.each do |word|
      @groups[self.class.abbreviate(word)][word] = true
    end
  end

  def isUnique(word)
    key = self.class.abbreviate(word)
    words = @groups[key]
    words.empty? || (words.length == 1 && words.key?(word))
  end

  def self.abbreviate(word)
    return word if word.length <= 2

    "#{word[0]}#{word.length - 2}#{word[-1]}"
  end
end
