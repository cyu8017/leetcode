# LeetCode 3643 - Flip Square Submatrix Vertically
# https://leetcode.com/problems/flip-square-submatrix-vertically/

# @param {Integer[][]} grid
# @param {Integer} x
# @param {Integer} y
# @param {Integer} k
# @return {Integer[][]}
def reverse_submatrix(grid, x, y, k)
  (x...(x + k / 2)).each do |i|
    i2 = x + k - 1 - (i - x)
    (y...(y + k)).each do |j|
      grid[i][j], grid[i2][j] = grid[i2][j], grid[i][j]
    end
  end
  grid
end
