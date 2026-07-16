# LeetCode 0130 - Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/

# @param {Character[][]} board
# @return {void}
def solve(board)
  return if board.empty? || board[0].empty?

  rows = board.length
  columns = board[0].length
  mark = lambda do |row, column|
    next if row.negative? || row >= rows || column.negative? || column >= columns
    next unless board[row][column] == "O"

    board[row][column] = "E"
    mark.call(row + 1, column)
    mark.call(row - 1, column)
    mark.call(row, column + 1)
    mark.call(row, column - 1)
  end

  rows.times { |row| mark.call(row, 0); mark.call(row, columns - 1) }
  columns.times { |column| mark.call(0, column); mark.call(rows - 1, column) }
  rows.times do |row|
    columns.times do |column|
      board[row][column] = "X" if board[row][column] == "O"
      board[row][column] = "O" if board[row][column] == "E"
    end
  end
end