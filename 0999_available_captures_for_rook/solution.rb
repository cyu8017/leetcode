# LeetCode 0999 - Available Captures for Rook
# https://leetcode.com/problems/available-captures-for-rook/

# @param {Character[][]} board
# @return {Integer}
def num_rook_captures(board)
  m = board.length
  n = board[0].length
  r = c = -1
  m.times do |i|
    board[i].length.times do |j|
      if board[i][j] == "R"
        r = i
        c = j
      end
    end
  end
  return 0 if r < 0

  ans = 0
  [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
    i = r + dr
    j = c + dc
    while i >= 0 && i < m && j >= 0 && j < board[i].length
      break if board[i][j] == "B"

      if board[i][j] == "p"
        ans += 1
        break
      end
      i += dr
      j += dc
    end
  end
  ans
end
