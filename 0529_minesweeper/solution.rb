# LeetCode 0529 - Minesweeper
# https://leetcode.com/problems/minesweeper/

class Solution
  DIRECTIONS = [
    [-1, -1], [-1, 0], [-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
  ].freeze

  def update_board(board, click)
    rows = board.length
    cols = board[0].length
    row, col = click

    if board[row][col] == "M"
      board[row][col] = "X"
      return board
    end

    reveal(board, row, col, rows, cols)
    board
  end

  alias_method :updateBoard, :update_board

  private

  def count_mines(board, r, c, rows, cols)
    total = 0
    DIRECTIONS.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      total += 1 if nr.between?(0, rows - 1) && nc.between?(0, cols - 1) && board[nr][nc] == "M"
    end
    total
  end

  def reveal(board, r, c, rows, cols)
    return unless r.between?(0, rows - 1) && c.between?(0, cols - 1) && board[r][c] == "E"

    mines = count_mines(board, r, c, rows, cols)
    board[r][c] = mines.zero? ? "B" : mines.to_s
    return unless mines.zero?

    DIRECTIONS.each do |dr, dc|
      reveal(board, r + dr, c + dc, rows, cols)
    end
  end
end
