# LeetCode 2257 - Count Unguarded Cells in the Grid
# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} guards
# @param {Integer[][]} walls
# @return {Integer}
def count_unguarded(m, n, guards, walls)
  grid = Array.new(m) { Array.new(n, 0) }
  walls.each { |r, c| grid[r][c] = 2 }
  guards.each { |r, c| grid[r][c] = 2 }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  guards.each do |gr, gc|
    dirs.each do |dr, dc|
      r = gr + dr
      c = gc + dc
      while r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != 2
        grid[r][c] = 1
        r += dr
        c += dc
      end
    end
  end
  ans = 0
  m.times do |i|
    n.times { |j| ans += 1 if grid[i][j] == 0 }
  end
  ans
end
