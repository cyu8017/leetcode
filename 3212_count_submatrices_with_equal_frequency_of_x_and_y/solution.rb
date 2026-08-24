# LeetCode 3212 - Count Submatrices With Equal Frequency of X and Y
# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

# @param {Character[][]} grid
# @return {Integer}
def number_of_submatrices(grid)
  m = grid.length
  n = grid[0].length
  s = Array.new(m + 1) { Array.new(n + 1) { [0, 0] } }
  ans = 0
  (1..m).each do |i|
    (1..n).each do |j|
      s[i][j][0] = s[i - 1][j][0] + s[i][j - 1][0] - s[i - 1][j - 1][0]
      s[i][j][0] += 1 if grid[i - 1][j - 1] == "X"
      s[i][j][1] = s[i - 1][j][1] + s[i][j - 1][1] - s[i - 1][j - 1][1]
      s[i][j][1] += 1 if grid[i - 1][j - 1] == "Y"
      ans += 1 if s[i][j][0] > 0 && s[i][j][0] == s[i][j][1]
    end
  end
  ans
end
