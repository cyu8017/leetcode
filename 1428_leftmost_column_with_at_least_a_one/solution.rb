# LeetCode 1428 - Leftmost Column With At Least A One
# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

def left_most_column_with_one(binary_matrix)
  rows, cols = binary_matrix.dimensions
  row = 0
  col = cols - 1
  answer = -1
  while row < rows && col >= 0
    if binary_matrix.get(row, col) == 1
      answer = col
      col -= 1
    else
      row += 1
    end
  end
  answer
end
