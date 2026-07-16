# LeetCode 0296 - Best Meeting Point
# https://leetcode.com/problems/best-meeting-point/

class Solution
  def minTotalDistance(grid)
    rows = []
    cols = []
    grid.each_with_index do |row, row_index|
      row.each_with_index do |value, col_index|
        next unless value == 1

        rows << row_index
        cols << col_index
      end
    end
    cols.sort!
    row_median = rows[rows.length / 2]
    col_median = cols[cols.length / 2]
    rows.sum { |row| (row - row_median).abs } + cols.sum { |col| (col - col_median).abs }
  end
end
