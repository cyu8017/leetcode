# LeetCode 1895 - Largest Magic Square
# https://leetcode.com/problems/largest-magic-square/

# @param {Integer[][]} grid
# @return {Integer}
def largest_magic_square(grid)
  rows = grid.length
  cols = grid[0].length
  row_prefix = Array.new(rows) { Array.new(cols + 1, 0) }
  col_prefix = Array.new(cols) { Array.new(rows + 1, 0) }

  (0...rows).each do |i|
    (0...cols).each do |j|
      row_prefix[i][j + 1] = row_prefix[i][j] + grid[i][j]
      col_prefix[j][i + 1] = col_prefix[j][i] + grid[i][j]
    end
  end

  row_sum = lambda { |row, col_start, col_end| row_prefix[row][col_end + 1] - row_prefix[row][col_start] }
  col_sum = lambda { |col, row_start, row_end| col_prefix[col][row_end + 1] - col_prefix[col][row_start] }

  is_magic = lambda do |row_start, col_start, size|
    target = row_sum.call(row_start, col_start, col_start + size - 1)
    (row_start...row_start + size).each do |row|
      return false if row_sum.call(row, col_start, col_start + size - 1) != target
    end
    (col_start...col_start + size).each do |col|
      return false if col_sum.call(col, row_start, row_start + size - 1) != target
    end
    diag1 = (0...size).sum { |offset| grid[row_start + offset][col_start + offset] }
    diag2 = (0...size).sum { |offset| grid[row_start + offset][col_start + size - 1 - offset] }
    diag1 == target && diag2 == target
  end

  [rows, cols].min.downto(1) do |size|
    (0..rows - size).each do |row_start|
      (0..cols - size).each do |col_start|
        return size if is_magic.call(row_start, col_start, size)
      end
    end
  end
  1
end
