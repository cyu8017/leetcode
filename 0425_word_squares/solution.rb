# LeetCode 0425 - Word Squares
# https://leetcode.com/problems/word-squares/

class Solution
  def word_squares(words)
    words.sort!
    length = words[0].length
    prefix_map = { "" => words.dup }
    words.each do |word|
      word.length.times do |index|
        prefix = word[0..index]
        prefix_map[prefix] ||= []
        prefix_map[prefix] << word
      end
    end

    squares = []
    current = []

    dfs = lambda do |row|
      if row == length
        squares << current.dup
        return
      end
      prefix = current.map { |word| word[row] }.join
      prefix_map.fetch(prefix, []).each do |candidate|
        current << candidate
        dfs.call(row + 1)
        current.pop
      end
    end

    dfs.call(0)
    squares
  end

  alias_method :wordSquares, :word_squares
end
