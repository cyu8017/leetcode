# LeetCode 2133 - Check if Every Row and Column Contains All Numbers
# https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

# @param {Integer[][]} matrix
# @return {Boolean}
def check_valid(matrix)
  n = matrix.length
  n.times do |i|
    row = Array.new(n + 1, false)
    col = Array.new(n + 1, false)
    n.times do |j|
      return false if row[matrix[i][j]] || col[matrix[j][i]]

      row[matrix[i][j]] = col[matrix[j][i]] = true
    end
  end
  true
end
