# LeetCode 0348 - Design Tic-Tac-Toe
# https://leetcode.com/problems/design-tic-tac-toe/

class TicTacToe
  def initialize(n)
    @n = n
    @rows = Array.new(n, 0)
    @cols = Array.new(n, 0)
    @diag = 0
    @anti_diag = 0
  end

  def move(row, col, player)
    add = player == 1 ? 1 : -1

    @rows[row] += add
    @cols[col] += add
    @diag += add if row == col
    @anti_diag += add if row + col == @n - 1

    if [@rows[row], @cols[col], @diag, @anti_diag].any? { |value| value.abs == @n }
      return player
    end

    0
  end
end
