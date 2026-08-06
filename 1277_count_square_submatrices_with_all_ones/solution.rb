# LeetCode 1277 - Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

# @param {Integer[][]} matrix
# @return {Integer}
def count_squares(matrix)
  answer = 0
  matrix.each_with_index do |row, r|
    row.each_with_index do |_, c|
      if matrix[r][c] == 1 && r > 0 && c > 0
        matrix[r][c] += [matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]].min
      end
      answer += matrix[r][c]
    end
  end
  answer
end
