# LeetCode 3148 - Maximum Difference Score in a Grid
# https://leetcode.com/problems/maximum-difference-score-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_score(grid)
  m = grid.length
  n = grid[0].length
  inf = 1 << 30
  f = Array.new(m) { Array.new(n, 0) }
  ans = -inf
  m.times do |i|
    n.times do |j|
      x = grid[i][j]
      mi = inf
      mi = [mi, f[i - 1][j]].min if i > 0
      mi = [mi, f[i][j - 1]].min if j > 0
      ans = [ans, x - mi].max
      f[i][j] = [x, mi].min
    end
  end
  ans
end
