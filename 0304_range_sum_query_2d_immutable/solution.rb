# LeetCode 0304 - Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix
  def initialize(matrix)
    rows = matrix.length
    cols = rows.zero? ? 0 : matrix[0].length
    @prefix = Array.new(rows + 1) { Array.new(cols + 1, 0) }
    rows.times do |row|
      cols.times do |col|
        @prefix[row + 1][col + 1] = matrix[row][col] +
                                     @prefix[row][col + 1] +
                                     @prefix[row + 1][col] -
                                     @prefix[row][col]
      end
    end
  end

  def sumRegion(row1, col1, row2, col2)
    top_left = @prefix[row1][col1]
    top_right = @prefix[row1][col2 + 1]
    bottom_left = @prefix[row2 + 1][col1]
    bottom_right = @prefix[row2 + 1][col2 + 1]
    bottom_right - top_right - bottom_left + top_left
  end
end
