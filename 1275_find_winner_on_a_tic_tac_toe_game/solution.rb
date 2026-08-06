# LeetCode 1275 - Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

# @param {Integer[][]} moves
# @return {String}
def tictactoe(moves)
  board = Array.new(3) { Array.new(3, 0) }
  moves.each_with_index do |(r, c), i|
    board[r][c] = i.even? ? 1 : -1
  end
  lines = board + board.transpose
  lines << [board[0][0], board[1][1], board[2][2]]
  lines << [board[0][2], board[1][1], board[2][0]]
  lines.each do |line|
    s = line.sum
    return "A" if s == 3
    return "B" if s == -3
  end
  moves.length == 9 ? "Draw" : "Pending"
end
