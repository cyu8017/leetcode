# LeetCode 2684 - Maximum Number of Moves in a Grid
# https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def max_moves(grid)
  m = grid.length
  n = grid[0].length
  dp = Array.new(m, 0)
  (n - 2).downto(0) do |c|
    ndp = Array.new(m, 0)
    m.times do |r|
      best = 0
      [-1, 0, 1].each do |dr|
        nr = r + dr
        best = [best, 1 + dp[nr]].max if nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c]
      end
      ndp[r] = best
    end
    dp = ndp
  end
  dp.max
end
