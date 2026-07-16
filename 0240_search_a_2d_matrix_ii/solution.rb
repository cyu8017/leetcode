# LeetCode 0240 - Search a 2D Matrix II
# https://leetcode.com/problems/search-a-2d-matrix-ii/

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  return false if matrix.empty? || matrix[0].empty?

  row = 0
  col = matrix[0].length - 1
  while row < matrix.length && col >= 0
    value = matrix[row][col]
    return true if value == target
    if value > target
      col -= 1
    else
      row += 1
    end
  end
  false
end
