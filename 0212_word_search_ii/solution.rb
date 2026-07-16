# LeetCode 0212 - Word Search II
# https://leetcode.com/problems/word-search-ii/

class TrieNode
  attr_accessor :children, :word

  def initialize
    @children = {}
    @word = nil
  end
end

class Solution
  def find_words(board, words)
    root = TrieNode.new
    words.each do |word|
      node = root
      word.each_char do |char|
        node.children[char] ||= TrieNode.new
        node = node.children[char]
      end
      node.word = word
    end

    rows = board.length
    cols = board[0].length
    result = {}

    dfs = lambda do |row, col, node|
      char = board[row][col]
      next_node = node.children[char]
      return unless next_node

      if next_node.word
        result[next_node.word] = true
        next_node.word = nil
      end
      board[row][col] = '#'
      dfs.call(row + 1, col, next_node) if row + 1 < rows && board[row + 1][col] != '#'
      dfs.call(row - 1, col, next_node) if row - 1 >= 0 && board[row - 1][col] != '#'
      dfs.call(row, col + 1, next_node) if col + 1 < cols && board[row][col + 1] != '#'
      dfs.call(row, col - 1, next_node) if col - 1 >= 0 && board[row][col - 1] != '#'
      board[row][col] = char
      node.children.delete(char) if next_node.children.empty?
    end

    rows.times do |row|
      cols.times do |col|
        dfs.call(row, col, root)
      end
    end
    result.keys
  end
end
