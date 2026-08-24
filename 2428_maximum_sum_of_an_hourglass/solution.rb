# LeetCode 2428 - Maximum Sum of an Hourglass
# https://leetcode.com/problems/maximum-sum-of-an-hourglass/

# @param {Integer[][]} grid
# @return {Integer}
def max_sum(grid)
  m = grid.length
  n = grid[0].length
  ans = -1 << 60
  (0...(m - 2)).each do |i|
    (0...(n - 2)).each do |j|
      s = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] +
          grid[i + 1][j + 1] +
          grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
      ans = s if s > ans
    end
  end
  ans
end
