# LeetCode 3128 - Right Triangles
# https://leetcode.com/problems/right-triangles/

# @param {Integer[][]} grid
# @return {Integer}
def number_of_right_triangles(grid)
  m = grid.length
  n = grid[0].length
  rows = Array.new(m, 0)
  cols = Array.new(n, 0)
  m.times do |i|
    n.times do |j|
      rows[i] += grid[i][j]
      cols[j] += grid[i][j]
    end
  end
  ans = 0
  m.times do |i|
    n.times do |j|
      ans += (rows[i] - 1) * (cols[j] - 1) if grid[i][j] == 1
    end
  end
  ans
end
