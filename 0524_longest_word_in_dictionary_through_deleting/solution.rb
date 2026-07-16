# LeetCode 0524 - Longest Word in Dictionary through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution
  def find_longest_word(s, dictionary)
    best = ""
    dictionary.each do |word|
      next unless subsequence?(s, word)

      if word.length > best.length || (word.length == best.length && word < best)
        best = word
      end
    end
    best
  end

  alias_method :findLongestWord, :find_longest_word

  private

  def subsequence?(source, word)
    index = 0
    source.each_char do |char|
      index += 1 if index < word.length && word[index] == char
    end
    index == word.length
  end
end
