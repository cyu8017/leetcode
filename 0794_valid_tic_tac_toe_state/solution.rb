# LeetCode 0794 - Valid Tic-Tac-Toe State
# https://leetcode.com/problems/valid-tic-tac-toe-state/

# @param {String[]} board
# @return {Boolean}
def valid_tic_tac_toe(board)
  flat = board.join
  x_count = flat.count("X")
  o_count = flat.count("O")
  return false unless [x_count, x_count - 1].include?(o_count)

  win = lambda do |player|
    lines = board.dup
    3.times { |c| lines << (0...3).map { |r| board[r][c] }.join }
    lines << board[0][0] + board[1][1] + board[2][2]
    lines << board[0][2] + board[1][1] + board[2][0]
    lines.any? { |line| line == player * 3 }
  end

  x_win = win.call("X")
  o_win = win.call("O")
  return false if x_win && o_win
  return false if x_win && x_count != o_count + 1
  return false if o_win && x_count != o_count

  true
end
