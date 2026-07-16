# LeetCode 0289 - Game of Life
# https://leetcode.com/problems/game-of-life/

class Solution
  def gameOfLife(board)
    rows = board.length
    cols = board[0].length
    (0...rows).each do |row|
      (0...cols).each do |col|
        live_neighbors = 0
        (-1..1).each do |dr|
          (-1..1).each do |dc|
            next if dr == 0 && dc == 0

            nr = row + dr
            nc = col + dc
            next unless nr.between?(0, rows - 1) && nc.between?(0, cols - 1)
            live_neighbors += 1 if board[nr][nc] & 1 == 1
          end
        end
        if (board[row][col] & 1) == 1 && [2, 3].include?(live_neighbors)
          board[row][col] |= 2
        elsif (board[row][col] & 1) == 0 && live_neighbors == 3
          board[row][col] |= 2
        end
      end
    end
    (0...rows).each do |row|
      (0...cols).each do |col|
        board[row][col] >>= 1
      end
    end
  end
end
