# LeetCode 3603 - Minimum Cost Path with Alternating Directions II
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} wait_cost
# @return {Integer}
def min_cost(m, n, wait_cost)
  entry = lambda { |i, j| (i + 1) * (j + 1) }
  inf = 10**18
  dp = Array.new(m) { Array.new(n, inf) }
  dp[0][0] = entry.call(0, 0)
  (0...m).each do |i|
    (0...n).each do |j|
      next if i == 0 && j == 0
      if i > 0
        cand = dp[i - 1][j] + entry.call(i, j)
        cand += wait_cost[i - 1][j] unless i - 1 == 0 && j == 0
        dp[i][j] = [dp[i][j], cand].min
      end
      if j > 0
        cand = dp[i][j - 1] + entry.call(i, j)
        cand += wait_cost[i][j - 1] unless i == 0 && j - 1 == 0
        dp[i][j] = [dp[i][j], cand].min
      end
    end
  end
  dp[m - 1][n - 1]
end
