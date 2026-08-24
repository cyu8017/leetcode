# LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

# @param {Integer[][]} grid
# @return {Integer[][]}
def ones_minus_zeros(grid)
  m = grid.length
  n = grid[0].length
  row = Array.new(m, 0)
  col = Array.new(n, 0)
  (0...m).each do |i|
    (0...n).each do |j|
      row[i] += grid[i][j]
      col[j] += grid[i][j]
    end
  end
  ans = Array.new(m) { Array.new(n, 0) }
  (0...m).each do |i|
    (0...n).each do |j|
      ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
    end
  end
  ans
end
