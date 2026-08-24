# LeetCode 3651 - Minimum Cost Path with Teleportations
# https://leetcode.com/problems/minimum-cost-path-with-teleportations/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def min_cost(grid, k)
  m = grid.length
  n = grid[0].length
  inf = 536870911
  f = Array.new(k + 1) { Array.new(m) { Array.new(n, inf) } }
  f[0][0][0] = 0
  (0...m).each do |i|
    (0...n).each do |j|
      f[0][i][j] = [f[0][i][j], f[0][i - 1][j] + grid[i][j]].min if i > 0
      f[0][i][j] = [f[0][i][j], f[0][i][j - 1] + grid[i][j]].min if j > 0
    end
  end
  g = {}
  (0...m).each do |i|
    (0...n).each do |j|
      (g[grid[i][j]] ||= []) << [i, j]
    end
  end
  keys = g.keys.sort.reverse
  (1..k).each do |t|
    mn = inf
    keys.each do |key|
      pos = g[key]
      pos.each { |p| mn = f[t - 1][p[0]][p[1]] if f[t - 1][p[0]][p[1]] < mn }
      pos.each { |p| f[t][p[0]][p[1]] = mn }
    end
    (0...m).each do |i|
      (0...n).each do |j|
        f[t][i][j] = [f[t][i][j], f[t][i - 1][j] + grid[i][j]].min if i > 0
        f[t][i][j] = [f[t][i][j], f[t][i][j - 1] + grid[i][j]].min if j > 0
      end
    end
  end
  ans = inf
  (0..k).each { |t| ans = f[t][m - 1][n - 1] if f[t][m - 1][n - 1] < ans }
  ans
end
