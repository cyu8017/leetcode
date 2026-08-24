# LeetCode 0892 - Surface Area of 3D Shapes
# https://leetcode.com/problems/surface-area-of-3d-shapes/

# @param {Integer[][]} grid
# @return {Integer}
def surface_area(grid)
  n = grid.length
  area = 0
  n.times do |i|
    n.times do |j|
      next if grid[i][j] == 0

      area += grid[i][j] * 4 + 2
      area -= [grid[i][j], grid[i - 1][j]].min * 2 if i > 0
      area -= [grid[i][j], grid[i][j - 1]].min * 2 if j > 0
    end
  end
  area
end
