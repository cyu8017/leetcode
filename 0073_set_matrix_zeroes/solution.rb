# LeetCode 0073 - Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/

# @param {Integer[][]} matrix
# @return {Void}
def set_zeroes(matrix)
  rows = matrix.length
  cols = matrix[0].length
  first_row_zero = matrix[0].any?(&:zero?)
  first_col_zero = matrix.any? { |row| row[0].zero? }

  (1...rows).each do |i|
    (1...cols).each do |j|
      if matrix[i][j].zero?
        matrix[i][0] = 0
        matrix[0][j] = 0
      end
    end
  end

  (1...rows).each do |i|
    (1...cols).each do |j|
      matrix[i][j] = 0 if matrix[i][0].zero? || matrix[0][j].zero?
    end
  end

  matrix[0].fill(0) if first_row_zero
  matrix.each { |row| row[0] = 0 } if first_col_zero
end
