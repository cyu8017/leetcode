# LeetCode 0840 - Magic Squares In Grid
# https://leetcode.com/problems/magic-squares-in-grid/

# @param {Integer[][]} grid
# @return {Integer}
def num_magic_squares_inside(grid)
  rows = grid.length
  cols = grid[0].length
  return 0 if rows < 3 || cols < 3

  magic = lambda do |r, c|
    vals = (0...3).flat_map { |i| (0...3).map { |j| grid[r + i][c + j] } }
    return false if vals.sort != (1..9).to_a

    a = grid
    a[r][c] + a[r][c + 1] + a[r][c + 2] == 15 &&
      a[r + 1][c] + a[r + 1][c + 1] + a[r + 1][c + 2] == 15 &&
      a[r + 2][c] + a[r + 2][c + 1] + a[r + 2][c + 2] == 15 &&
      a[r][c] + a[r + 1][c] + a[r + 2][c] == 15 &&
      a[r][c + 1] + a[r + 1][c + 1] + a[r + 2][c + 1] == 15 &&
      a[r][c + 2] + a[r + 1][c + 2] + a[r + 2][c + 2] == 15 &&
      a[r][c] + a[r + 1][c + 1] + a[r + 2][c + 2] == 15 &&
      a[r][c + 2] + a[r + 1][c + 1] + a[r + 2][c] == 15
  end

  (0...rows - 2).sum { |i| (0...cols - 2).count { |j| magic.call(i, j) } }
end
