# LeetCode 0883 - Projection Area of 3D Shapes
# https://leetcode.com/problems/projection-area-of-3d-shapes/

# @param {Integer[][]} grid
# @return {Integer}
def projection_area(grid)
  n = grid.length
  top = 0
  n.times { |i| n.times { |j| top += 1 if grid[i][j] != 0 } }
  front = grid.sum { |row| row.max }
  side = (0...n).sum { |j| (0...n).map { |i| grid[i][j] }.max }
  top + front + side
end
