# LeetCode 0291 - Word Pattern II
# https://leetcode.com/problems/word-pattern-ii/

class Solution
  def wordPatternMatch(pattern, s)
    char_to_word = {}
    word_to_char = {}

    backtrack = lambda do |pattern_index, string_index|
      return string_index == s.length if pattern_index == pattern.length

      char = pattern[pattern_index]
      if char_to_word.key?(char)
        word = char_to_word[char]
        return false unless s.start_with?(word, string_index)

        return backtrack.call(pattern_index + 1, string_index + word.length)
      end

      (string_index + 1..s.length).each do |end_index|
        word = s[string_index...end_index]
        next if word_to_char.key?(word)

        char_to_word[char] = word
        word_to_char[word] = char
        return true if backtrack.call(pattern_index + 1, end_index)

        char_to_word.delete(char)
        word_to_char.delete(word)
      end
      false
    end

    backtrack.call(0, 0)
  end
end
