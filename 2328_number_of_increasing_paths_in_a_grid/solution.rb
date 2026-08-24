# LeetCode 2328 - Number of Increasing Paths in a Grid
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def count_paths(grid)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n, 0) }
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  dfs = lambda do |r, c|
    return dp[r][c] if dp[r][c] != 0
    res = 1
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c]
        res = (res + dfs.call(nr, nc)) % mod
      end
    end
    dp[r][c] = res
    res
  end
  ans = 0
  (0...m).each do |i|
    (0...n).each { |j| ans = (ans + dfs.call(i, j)) % mod }
  end
  ans
end
