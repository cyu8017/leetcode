# LeetCode 3665 - Twisted Mirror Path Count
# https://leetcode.com/problems/twisted-mirror-path-count/

# @param {Integer[][]} grid
# @return {Integer}
def unique_paths(grid)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  next_cell = lambda do |i, j, di, dj|
    ni = i + di
    nj = j + dj
    while ni >= 0 && ni < m && nj >= 0 && nj < n && grid[ni][nj] == 1
      if dj == 1
        di = 1
        dj = 0
      else
        di = 0
        dj = 1
      end
      ni += di
      nj += dj
    end
    return nil if ni < 0 || nj < 0 || ni >= m || nj >= n

    [ni, nj]
  end
  dp = Array.new(m) { Array.new(n, 0) }
  return 0 if grid[0][0] == 1

  dp[0][0] = 1
  (0...m).each do |i|
    (0...n).each do |j|
      next if grid[i][j] == 1 || dp[i][j] == 0

      a = next_cell.call(i, j, 0, 1)
      dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % mod if a
      b = next_cell.call(i, j, 1, 0)
      dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % mod if b
    end
  end
  dp[m - 1][n - 1]
end
