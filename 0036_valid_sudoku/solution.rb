# LeetCode 0036 - Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

# @param {Character[][]} board
# @return {Boolean}
def is_valid_sudoku(board)
  rows = Array.new(9) { {} }
  cols = Array.new(9) { {} }
  boxes = Array.new(9) { {} }

  9.times do |r|
    9.times do |c|
      value = board[r][c]
      next if value == "."

      box = (r / 3) * 3 + c / 3
      return false if rows[r][value] || cols[c][value] || boxes[box][value]

      rows[r][value] = true
      cols[c][value] = true
      boxes[box][value] = true
    end
  end

  true
end
