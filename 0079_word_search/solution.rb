# LeetCode 0079 - Word Search
# https://leetcode.com/problems/word-search/

# @param {Character[][]} board
# @param {String} word
# @return {Boolean}
def exist(board, word)
  rows = board.length
  cols = board[0].length

  dfs = lambda do |row, col, index|
    return true if index == word.length
    return false if row.negative? || col.negative? || row >= rows || col >= cols
    return false if board[row][col] != word[index]

    temp = board[row][col]
    board[row][col] = '#'

    found = dfs.call(row + 1, col, index + 1) ||
            dfs.call(row - 1, col, index + 1) ||
            dfs.call(row, col + 1, index + 1) ||
            dfs.call(row, col - 1, index + 1)

    board[row][col] = temp
    found
  end

  (0...rows).each do |row|
    (0...cols).each do |col|
      return true if dfs.call(row, col, 0)
    end
  end

  false
end
