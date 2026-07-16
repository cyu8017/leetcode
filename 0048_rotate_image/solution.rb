# LeetCode 0048 - Rotate Image
# https://leetcode.com/problems/rotate-image/

# @param {Integer[][]} matrix
# @return {Void}
def rotate(matrix)
  n = matrix.length

  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    end
  end

  matrix.each(&:reverse!)
end
