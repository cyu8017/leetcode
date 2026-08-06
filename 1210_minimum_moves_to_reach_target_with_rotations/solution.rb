# LeetCode 1210 - Minimum Moves to Reach Target with Rotations
# https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

require "set"

# @param {Integer[][]} grid
# @return {Integer}
def minimum_moves(grid)
  n = grid.length
  start = [0, 0, 0]
  target = [n - 1, n - 2, 0]
  q = [[start, 0]]
  seen = Set[start]
  until q.empty?
    state, moves = q.shift
    r, c, orient = state
    return moves if state == target
    nxt = []
    if orient == 0
      nxt << [r, c + 1, 0] if c + 2 < n && grid[r][c + 2] == 0
      if r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0
        nxt << [r + 1, c, 0]
        nxt << [r, c, 1]
      end
    else
      nxt << [r + 1, c, 1] if r + 2 < n && grid[r + 2][c] == 0
      if c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0
        nxt << [r, c + 1, 1]
        nxt << [r, c, 0]
      end
    end
    nxt.each do |st|
      next if seen.include?(st)
      seen.add(st)
      q << [st, moves + 1]
    end
  end
  -1
end
