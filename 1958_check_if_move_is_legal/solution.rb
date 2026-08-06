# LeetCode 1958 - Check if Move is Legal
# https://leetcode.com/problems/check-if-move-is-legal/

# @param {Character[][]} board
# @param {Integer} r_move
# @param {Integer} c_move
# @param {Character} color
# @return {Boolean}
def check_move(board, r_move, c_move, color)
  opp = color == "B" ? "W" : "B"
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
  dirs.each do |dr, dc|
    r = r_move + dr
    c = c_move + dc
    steps = 0
    while r.between?(0, 7) && c.between?(0, 7) && board[r][c] == opp
      r += dr
      c += dc
      steps += 1
    end
    return true if steps.positive? && r.between?(0, 7) && c.between?(0, 7) && board[r][c] == color
  end
  false
end
