# LeetCode 2371 - Minimize Maximum Value in a Grid
# https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

# @param {Integer[][]} grid
# @return {Integer[][]}
def min_score(grid)
  m = grid.length
  n = grid[0].length
  arr = []
  (0...m).each do |i|
    (0...n).each { |j| arr << [grid[i][j], i, j] }
  end
  arr.sort_by! { |x| x[0] }
  row_max = Array.new(m, 0)
  col_max = Array.new(n, 0)
  ans = Array.new(m) { Array.new(n, 0) }
  arr.each do |_, i, j|
    val = [row_max[i], col_max[j]].max + 1
    ans[i][j] = val
    row_max[i] = val
    col_max[j] = val
  end
  ans
end

alias solve min_score
