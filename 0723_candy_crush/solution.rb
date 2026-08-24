# LeetCode 0723 - Candy Crush
# https://leetcode.com/problems/candy-crush/

# @param {Integer[][]} board
# @return {Integer[][]}
def candy_crush(board)
  m = board.length
  n = board[0].length
  stable = false
  until stable
    stable = true
    m.times do |i|
      (0...(n - 2)).each do |j|
        value = board[i][j].abs
        if value != 0 && value == board[i][j + 1].abs && value == board[i][j + 2].abs
          board[i][j] = board[i][j + 1] = board[i][j + 2] = -value
          stable = false
        end
      end
    end
    n.times do |j|
      (0...(m - 2)).each do |i|
        value = board[i][j].abs
        if value != 0 && value == board[i + 1][j].abs && value == board[i + 2][j].abs
          board[i][j] = board[i + 1][j] = board[i + 2][j] = -value
          stable = false
        end
      end
    end

    n.times do |j|
      write = m - 1
      (m - 1).downto(0) do |i|
        if board[i][j] > 0
          board[write][j] = board[i][j]
          write -= 1
        end
      end
      write.downto(0) { |i| board[i][j] = 0 }
    end
  end
  board
end
