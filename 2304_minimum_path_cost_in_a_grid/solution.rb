# LeetCode 2304 - Minimum Path Cost in a Grid
# https://leetcode.com/problems/minimum-path-cost-in-a-grid/

# @param {Integer[][]} grid
# @param {Integer[][]} move_cost
# @return {Integer}
def min_path_cost(grid, move_cost)
  m = grid.length
  n = grid[0].length
  dp = grid[0].dup
  (0...m - 1).each do |r|
    nxt = Array.new(n, 2147483647 / 2)
    (0...n).each do |c|
      frm = grid[r][c]
      (0...n).each do |nc|
        nxt[nc] = [nxt[nc], dp[c] + move_cost[frm][nc] + grid[r + 1][nc]].min
      end
    end
    dp = nxt
  end
  ans = dp[0]
  (1...n).each { |i| ans = [ans, dp[i]].min }
  ans
end
