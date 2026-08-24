# LeetCode 3402 - Minimum Operations to Make Columns Strictly Increasing
# https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_operations(grid)
  m = grid.length
  n = grid[0].length
  ans = 0
  (0...n).each do |j|
    (1...m).each do |i|
      if grid[i][j] <= grid[i - 1][j]
        need = grid[i - 1][j] + 1
        ans += need - grid[i][j]
        grid[i][j] = need
      end
    end
  end
  ans
end
