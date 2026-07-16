# LeetCode 0037 - Sudoku Solver
# https://leetcode.com/problems/sudoku-solver/

# @param {Character[][]} board
# @return {Void} Do not return value, modify board in-place instead.
def solve_sudoku(board)
  rows = Array.new(9) { {} }
  cols = Array.new(9) { {} }
  boxes = Array.new(9) { {} }
  empty = []

  9.times do |r|
    9.times do |c|
      value = board[r][c]
      if value == "."
        empty << [r, c]
        next
      end
      box = (r / 3) * 3 + c / 3
      rows[r][value] = true
      cols[c][value] = true
      boxes[box][value] = true
    end
  end

  backtrack = lambda do |index|
    return true if index == empty.length

    r, c = empty[index]
    box = (r / 3) * 3 + c / 3
    (1..9).each do |n|
      digit = n.to_s
      next if rows[r][digit] || cols[c][digit] || boxes[box][digit]

      board[r][c] = digit
      rows[r][digit] = true
      cols[c][digit] = true
      boxes[box][digit] = true

      return true if backtrack.call(index + 1)

      board[r][c] = "."
      rows[r].delete(digit)
      cols[c].delete(digit)
      boxes[box].delete(digit)
    end

    false
  end

  backtrack.call(0)
end
