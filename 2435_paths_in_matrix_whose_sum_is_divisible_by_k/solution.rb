# LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
# https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def number_of_paths(grid, k)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n) { Array.new(k, 0) } }
  dp[0][0][grid[0][0] % k] = 1
  (0...m).each do |i|
    (0...n).each do |j|
      (0...k).each do |r|
        next if dp[i][j][r] == 0

        if i + 1 < m
          nr = (r + grid[i + 1][j]) % k
          dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod
        end
        if j + 1 < n
          nr = (r + grid[i][j + 1]) % k
          dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod
        end
      end
    end
  end
  dp[m - 1][n - 1][0]
end
