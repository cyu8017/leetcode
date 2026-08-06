# LeetCode 1329 - Sort The Matrix Diagonally
# https://leetcode.com/problems/sort-the-matrix-diagonally/

def diagonal_sort(mat)
  diagonals = Hash.new { |h, k| h[k] = [] }
  mat.each_with_index do |row, r|
    row.each_with_index { |value, c| diagonals[r - c] << value }
  end
  diagonals.each_value { |values| values.sort!.reverse! }
  mat.each_with_index do |row, r|
    row.each_index { |c| mat[r][c] = diagonals[r - c].pop }
  end
  mat
end
