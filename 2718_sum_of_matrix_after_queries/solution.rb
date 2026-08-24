# LeetCode 2718 - Sum of Matrix After Queries
# https://leetcode.com/problems/sum-of-matrix-after-queries/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer}
def matrix_sum_queries(n, queries)
  row_done = Array.new(n, false)
  col_done = Array.new(n, false)
  rows_left = n
  cols_left = n
  ans = 0
  (queries.length - 1).downto(0) do |i|
    typ, idx, val = queries[i]
    if typ == 0
      unless row_done[idx]
        ans += val * cols_left
        row_done[idx] = true
        rows_left -= 1
      end
    else
      unless col_done[idx]
        ans += val * rows_left
        col_done[idx] = true
        cols_left -= 1
      end
    end
  end
  ans
end
