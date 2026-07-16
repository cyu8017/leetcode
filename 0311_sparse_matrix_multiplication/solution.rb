# LeetCode 0311 - Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/

class Solution
  def multiply(mat1, mat2)
    rows = mat1.length
    inner = mat1[0].length
    cols = mat2[0].length
    result = Array.new(rows) { Array.new(cols, 0) }
    (0...rows).each do |row|
      (0...inner).each do |index|
        next if mat1[row][index] == 0

        (0...cols).each do |col|
          next if mat2[index][col] == 0

          result[row][col] += mat1[row][index] * mat2[index][col]
        end
      end
    end
    result
  end
end
