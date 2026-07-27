# LeetCode 1605 - Find Valid Matrix Given Row and Column Sums
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

# @param {Integer[]} row_sum
# @param {Integer[]} col_sum
# @return {Integer[][]}
def restore_matrix(row_sum, col_sum)
  row_sum = row_sum.dup
  col_sum = col_sum.dup
  ans = Array.new(row_sum.length) { Array.new(col_sum.length, 0) }
  i = j = 0
  while i < row_sum.length && j < col_sum.length
    x = [row_sum[i], col_sum[j]].min
    ans[i][j] = x
    row_sum[i] -= x
    col_sum[j] -= x
    i += 1 if row_sum[i].zero?
    j += 1 if col_sum[j].zero?
  end
  ans
end
