# LeetCode 0782 - Transform to Chessboard
# https://leetcode.com/problems/transform-to-chessboard/

# @param {Integer[][]} board
# @return {Integer}
def moves_to_chessboard(board)
  n = board.length
  n.times do |i|
    n.times do |j|
      if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0
        return -1
      end
    end
  end

  row_sum = board[0].sum
  col_sum = board.sum { |row| row[0] }
  return -1 unless (n / 2) <= row_sum && row_sum <= (n + 1) / 2
  return -1 unless (n / 2) <= col_sum && col_sum <= (n + 1) / 2

  row_swap = (0...n).count { |i| board[0][i] != i % 2 }
  col_swap = (0...n).count { |i| board[i][0] != i % 2 }
  if n.odd?
    row_swap = n - row_swap if row_swap.odd?
    col_swap = n - col_swap if col_swap.odd?
  else
    row_swap = [row_swap, n - row_swap].min
    col_swap = [col_swap, n - col_swap].min
  end
  (row_swap + col_swap) / 2
end
