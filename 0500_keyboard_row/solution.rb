# LeetCode 0500 - Keyboard Row
# https://leetcode.com/problems/keyboard-row/

require "set"

class Solution
  def find_words(words)
    rows = [
      "qwertyuiop".chars.to_set,
      "asdfghjkl".chars.to_set,
      "zxcvbnm".chars.to_set
    ]

    on_one_row = lambda do |word|
      letters = word.each_char.select(&:match?(/[a-zA-Z]/)).map { |ch| ch.downcase }.to_set
      rows.any? { |row| letters <= row }
    end

    words.select { |word| on_one_row.call(word) }
  end

  alias_method :findWords, :find_words
end
