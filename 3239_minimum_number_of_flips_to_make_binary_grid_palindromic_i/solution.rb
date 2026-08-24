# LeetCode 3239 - Minimum Number of Flips to Make Binary Grid Palindromic I
# https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/

# @param {Integer[][]} grid
# @return {Integer}
def min_flips(grid)
  m = grid.length
  n = grid[0].length
  cnt1 = cnt2 = 0
  grid.each do |row|
    (0...(n / 2)).each { |j| cnt1 += 1 if row[j] != row[n - j - 1] }
  end
  (0...n).each do |j|
    (0...(m / 2)).each { |i| cnt2 += 1 if grid[i][j] != grid[m - i - 1][j] }
  end
  [cnt1, cnt2].min
end
