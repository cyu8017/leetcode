# LeetCode 2661 - First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/

# @param {Integer[]} arr
# @param {Integer[][]} mat
# @return {Integer}
def first_complete_index(arr, mat)
  m = mat.length
  n = mat[0].length
  pos_r = Array.new(m * n + 1, 0)
  pos_c = Array.new(m * n + 1, 0)
  m.times do |i|
    n.times do |j|
      pos_r[mat[i][j]] = i
      pos_c[mat[i][j]] = j
    end
  end
  row_cnt = Array.new(m, 0)
  col_cnt = Array.new(n, 0)
  arr.each_with_index do |val, i|
    r = pos_r[val]
    c = pos_c[val]
    row_cnt[r] += 1
    col_cnt[c] += 1
    return i if row_cnt[r] == n || col_cnt[c] == m
  end
  -1
end
