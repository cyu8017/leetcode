# LeetCode 1572 - Matrix Diagonal Sum
# https://leetcode.com/problems/matrix-diagonal-sum/

# @param {Integer[][]} mat
# @return {Integer}
def diagonal_sum(mat)
  n = mat.length
  sum = (0...n).sum { |i| mat[i][i] + mat[i][n - 1 - i] }
  n.odd? ? sum - mat[n / 2][n / 2] : sum
end
