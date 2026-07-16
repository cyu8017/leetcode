# LeetCode 0051 - N-Queens
# https://leetcode.com/problems/n-queens/

# @param {Integer} n
# @return {String[][]}
def solve_n_queens(n)
  result = []
  cols = {}
  diag1 = {}
  diag2 = {}
  board = Array.new(n, '.' * n)

  backtrack = lambda do |row|
    if row == n
      result << board.dup
      return
    end

    (0...n).each do |col|
      next if cols[col] || diag1[row + col] || diag2[row - col]

      cols[col] = true
      diag1[row + col] = true
      diag2[row - col] = true

      row_chars = board[row].chars
      row_chars[col] = 'Q'
      board[row] = row_chars.join

      backtrack.call(row + 1)

      cols.delete(col)
      diag1.delete(row + col)
      diag2.delete(row - col)
      board[row] = '.' * n
    end
  end

  backtrack.call(0)
  result
end
