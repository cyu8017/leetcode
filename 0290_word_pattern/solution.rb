# LeetCode 0290 - Word Pattern
# https://leetcode.com/problems/word-pattern/

class Solution
  def wordPattern(pattern, s)
    words = s.split
    return false if pattern.length != words.length

    char_to_word = {}
    word_to_char = {}
    pattern.chars.zip(words).each do |char, word|
      if char_to_word.key?(char)
        return false if char_to_word[char] != word
      elsif word_to_char.key?(word)
        return false
      else
        char_to_word[char] = word
        word_to_char[word] = char
      end
    end
    true
  end
end
