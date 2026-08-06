# LeetCode 1582 - Special Positions in a Binary Matrix
# https://leetcode.com/problems/special-positions-in-a-binary-matrix/

# @param {Integer[][]} mat
# @return {Integer}
def num_special(mat)
  rows = mat.map(&:sum)
  cols = mat.transpose.map(&:sum)
  count = 0
  mat.each_with_index do |row, i|
    row.each_with_index do |val, j|
      count += 1 if val == 1 && rows[i] == 1 && cols[j] == 1
    end
  end
  count
end
