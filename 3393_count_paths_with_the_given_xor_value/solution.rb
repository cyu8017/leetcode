# LeetCode 3393 - Count Paths With the Given XOR Value
# https://leetcode.com/problems/count-paths-with-the-given-xor-value/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_paths_with_xor_value(grid, k)
  mod = 1_000_000_007
  m = grid.length
  n = grid[0].length
  dp = Array.new(m) { Array.new(n) { Array.new(16, 0) } }
  dp[0][0][grid[0][0]] = 1
  m.times do |i|
    n.times do |j|
      16.times do |x|
        next if dp[i][j][x] == 0

        if i + 1 < m
          nx = x ^ grid[i + 1][j]
          dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod
        end
        if j + 1 < n
          nx = x ^ grid[i][j + 1]
          dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod
        end
      end
    end
  end
  dp[m - 1][n - 1][k]
end
