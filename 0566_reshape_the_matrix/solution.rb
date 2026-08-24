# LeetCode 0566 - Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/

# @param {Integer[][]} mat
# @param {Integer} r
# @param {Integer} c
# @return {Integer[][]}
def matrix_reshape(mat, r, c)
  rows = mat.length
  cols = mat[0].length
  return mat if rows * cols != r * c

  flat = mat.flatten
  Array.new(r) { |i| flat[i * c, c] }
end
