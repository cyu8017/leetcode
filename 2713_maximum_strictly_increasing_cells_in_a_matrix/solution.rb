# LeetCode 2713 - Maximum Strictly Increasing Cells in a Matrix
# https://leetcode.com/problems/maximum-strictly-increasing-cells-in-a-matrix/

# @param {Integer[][]} mat
# @return {Integer}
def max_increasing_cells(mat)
  m = mat.length
  n = mat[0].length
  cells = []
  m.times { |i| n.times { |j| cells << [mat[i][j], i, j] } }
  cells.sort_by! { |x| x[0] }
  row_max = Array.new(m, 0)
  col_max = Array.new(n, 0)
  dp = Array.new(m) { Array.new(n, 0) }
  ans = 0
  i = 0
  while i < cells.length
    j = i
    j += 1 while j < cells.length && cells[j][0] == cells[i][0]
    buf = []
    (i...j).each do |k|
      r = cells[k][1]
      c = cells[k][2]
      best = [row_max[r], col_max[c]].max
      dp[r][c] = best + 1
      ans = [ans, dp[r][c]].max
      buf << [r, c, dp[r][c]]
    end
    buf.each do |r, c, v|
      row_max[r] = [row_max[r], v].max
      col_max[c] = [col_max[c], v].max
    end
    i = j
  end
  ans
end
