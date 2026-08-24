# LeetCode 2643 - Row With Maximum Ones
# https://leetcode.com/problems/row-with-maximum-ones/

# @param {Integer[][]} mat
# @return {Integer[]}
def row_and_maximum_ones(mat)
  best_row = 0
  best_cnt = -1
  mat.each_with_index do |row, i|
    cnt = row.sum
    if cnt > best_cnt
      best_cnt = cnt
      best_row = i
    end
  end
  [best_row, best_cnt]
end
