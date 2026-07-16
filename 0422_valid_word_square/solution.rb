# LeetCode 0422 - Valid Word Square
# https://leetcode.com/problems/valid-word-square/

class Solution
  def valid_word_square(words)
    words.each_with_index do |word, row|
      word.each_char.with_index do |char, col|
        return false if col >= words.length
        return false if row >= words[col].length
        return false if words[col][row] != char
      end
    end
    true
  end

  alias_method :validWordSquare, :valid_word_square
end
