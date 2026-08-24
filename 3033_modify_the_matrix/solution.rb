# LeetCode 3033 - Modify the Matrix
# https://leetcode.com/problems/modify-the-matrix/

# @param {Integer[][]} matrix
# @return {Integer[][]}
def modified_matrix(matrix)
  m = matrix.length
  n = matrix[0].length
  n.times do |j|
    mx = -1
    m.times { |i| mx = matrix[i][j] if matrix[i][j] > mx }
    m.times { |i| matrix[i][j] = mx if matrix[i][j] == -1 }
  end
  matrix
end
