# LeetCode 0054 - Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/

# @param {Integer[][]} matrix
# @return {Integer[]}
def spiral_order(matrix)
  return [] if matrix.empty?

  top = 0
  bottom = matrix.length - 1
  left = 0
  right = matrix[0].length - 1
  result = []

  while top <= bottom && left <= right
    (left..right).each { |col| result << matrix[top][col] }
    top += 1

    (top..bottom).each { |row| result << matrix[row][right] }
    right -= 1

    if top <= bottom
      right.downto(left) { |col| result << matrix[bottom][col] }
      bottom -= 1
    end

    if left <= right
      bottom.downto(top) { |row| result << matrix[row][left] }
      left += 1
    end
  end

  result
end
