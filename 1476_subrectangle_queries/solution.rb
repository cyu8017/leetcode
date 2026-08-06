# LeetCode 1476 - Subrectangle Queries
# https://leetcode.com/problems/subrectangle-queries/

class SubrectangleQueries
  def initialize(rectangle)
    @rectangle = rectangle
  end

  def update_subrectangle(row1, col1, row2, col2, new_value)
    (row1..row2).each do |r|
      (col1..col2).each { |c| @rectangle[r][c] = new_value }
    end
  end

  def get_value(row, col)
    @rectangle[row][col]
  end
end
