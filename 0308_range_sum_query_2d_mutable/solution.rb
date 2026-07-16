# LeetCode 0308 - Range Sum Query 2D - Mutable
# https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix
  def initialize(matrix)
    @matrix = matrix
    @rows = matrix.length
    @cols = @rows.zero? ? 0 : matrix[0].length
    @tree = Array.new(@rows + 1) { Array.new(@cols + 1, 0) }
    @rows.times do |row|
      @cols.times do |col|
        add(row + 1, col + 1, matrix[row][col])
      end
    end
  end

  def update(row, col, val)
    delta = val - @matrix[row][col]
    @matrix[row][col] = val
    add(row + 1, col + 1, delta)
  end

  def sumRegion(row1, col1, row2, col2)
    prefix(row2 + 1, col2 + 1) - prefix(row1, col2 + 1) - prefix(row2 + 1, col1) + prefix(row1, col1)
  end

  private

  def add(row, col, delta)
    row_index = row
    while row_index <= @rows
      col_index = col
      while col_index <= @cols
        @tree[row_index][col_index] += delta
        col_index += col_index & -col_index
      end
      row_index += row_index & -row_index
    end
  end

  def prefix(row, col)
    total = 0
    row_index = row
    while row_index.positive?
      col_index = col
      while col_index.positive?
        total += @tree[row_index][col_index]
        col_index -= col_index & -col_index
      end
      row_index -= row_index & -row_index
    end
    total
  end
end
