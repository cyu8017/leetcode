# LeetCode 0419 - Battleships in a Board
# https://leetcode.com/problems/battleships-in-a-board/

class Solution
  def count_battleships(board)
    count = 0
    board.each_with_index do |row_values, row|
      row_values.each_with_index do |cell, col|
        next unless cell == "X"
        next if row.positive? && board[row - 1][col] == "X"
        next if col.positive? && board[row][col - 1] == "X"

        count += 1
      end
    end
    count
  end

  alias_method :countBattleships, :count_battleships
end
