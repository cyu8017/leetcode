# LeetCode 3882 - Minimum XOR Path in a Grid
# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer}
def min_xor(grid)
  rows = grid.length
  cols = grid[0].length
  dp = Array.new(cols) { Array.new(1024, false) }
  rows.times do |row|
    left = Array.new(1024, false)
    cols.times do |col|
      nxt = Array.new(1024, false)
      value = grid[row][col]
      if row == 0 && col == 0
        nxt[value] = true
      else
        1024.times do |xorv|
          nxt[xorv ^ value] = true if dp[col][xorv] || left[xorv]
        end
      end
      dp[col] = nxt
      left = nxt
    end
  end
  1024.times { |xorv| return xorv if dp[cols - 1][xorv] }
  -1
end
