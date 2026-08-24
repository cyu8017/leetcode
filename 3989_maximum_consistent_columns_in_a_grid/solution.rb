# LeetCode 3989 - Maximum Consistent Columns in a Grid
# https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer} limit
# @return {Integer}
def max_consistent_columns(grid, limit)
  m = grid.length
  n = grid[0].length
  dp = Array.new(n, 0)
  ans = 1
  n.times do |j|
    dp[j] = 1
    j.times do |i|
      next if dp[i] + 1 <= dp[j]
      ok = true
      m.times do |r|
        d = (grid[r][j] - grid[r][i]).abs
        if d > limit
          ok = false
          break
        end
      end
      dp[j] = dp[i] + 1 if ok
    end
    ans = dp[j] if dp[j] > ans
  end
  ans
end
