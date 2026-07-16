# LeetCode 0498 - Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/

class Solution
  def find_diagonal_order(mat)
    return [] if mat.empty? || mat[0].empty?

    rows = mat.length
    cols = mat[0].length
    result = []
    row = 0
    col = 0
    upward = true

    (rows * cols).times do
      result << mat[row][col]
      if upward
        if col == cols - 1
          row += 1
          upward = false
        elsif row == 0
          col += 1
          upward = false
        else
          row -= 1
          col += 1
        end
      elsif row == rows - 1
        col += 1
        upward = true
      elsif col == 0
        row += 1
        upward = true
      else
        row += 1
        col -= 1
      end
    end
    result
  end

  alias_method :findDiagonalOrder, :find_diagonal_order
end
