# LeetCode 0676 - Implement Magic Dictionary
# https://leetcode.com/problems/implement-magic-dictionary/

class MagicDictionary
  def initialize
    @words = []
  end

  def build_dict(dictionary)
    @words = dictionary
    nil
  end

  def search(search_word)
    @words.any? do |word|
      next false if word.length != search_word.length

      diffs = 0
      word.length.times { |i| diffs += 1 if word[i] != search_word[i] }
      diffs == 1
    end
  end
end
