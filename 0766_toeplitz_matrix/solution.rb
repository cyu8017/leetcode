# LeetCode 0766 - Toeplitz Matrix
# https://leetcode.com/problems/toeplitz-matrix/

# @param {Integer[][]} matrix
# @return {Boolean}
def is_toeplitz_matrix(matrix)
  (1...matrix.length).each do |r|
    (1...matrix[0].length).each do |c|
      return false if matrix[r][c] != matrix[r - 1][c - 1]
    end
  end
  true
end
