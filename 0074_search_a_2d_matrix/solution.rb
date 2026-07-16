# LeetCode 0074 - Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

# @param {Integer[][]} matrix
# @param {Integer} target
# @return {Boolean}
def search_matrix(matrix, target)
  row = 0
  col = matrix[0].length - 1

  while row < matrix.length && col >= 0
    if matrix[row][col] == target
      return true
    elsif matrix[row][col] > target
      col -= 1
    else
      row += 1
    end
  end

  false
end
