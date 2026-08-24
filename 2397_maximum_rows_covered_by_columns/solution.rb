# LeetCode 2397 - Maximum Rows Covered by Columns
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

# @param {Integer[][]} matrix
# @param {Integer} num_select
# @return {Integer}
def maximum_rows(matrix, num_select)
  m = matrix.length
  n = matrix[0].length
  ans = [0]
  dfs = lambda do |col, chosen, mask|
    if chosen == num_select
      covered = 0
      (0...m).each do |i|
        ok = true
        (0...n).each do |j|
          if matrix[i][j] == 1 && ((mask >> j) & 1) == 0
            ok = false
            break
          end
        end
        covered += 1 if ok
      end
      ans[0] = covered if covered > ans[0]
      return
    end
    return if col == n
    dfs.call(col + 1, chosen + 1, mask | (1 << col))
    dfs.call(col + 1, chosen, mask)
  end
  dfs.call(0, 0, 0)
  ans[0]
end
