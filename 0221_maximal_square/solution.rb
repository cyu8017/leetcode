# LeetCode 0221 - Maximal Square
# https://leetcode.com/problems/maximal-square/

# @param {character[][]} matrix
# @return {Integer}
def maximal_square(matrix)
  return 0 if matrix.nil? || matrix.empty?

  rows = matrix.length
  cols = matrix[0].length
  dp = Array.new(cols + 1, 0)
  max_side = 0
  prev = 0
  (1..rows).each do |row|
    (1..cols).each do |col|
      temp = dp[col]
      if matrix[row - 1][col - 1] == "1"
        dp[col] = [dp[col], dp[col - 1], prev].min + 1
        max_side = [max_side, dp[col]].max
      else
        dp[col] = 0
      end
      prev = temp
    end
  end
  max_side * max_side
end
