# LeetCode 0861 - Score After Flipping Matrix
# https://leetcode.com/problems/score-after-flipping-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def matrix_score(grid)
  m = grid.length
  n = grid[0].length
  grid.each do |row|
    next unless row[0] == 0

    n.times { |j| row[j] ^= 1 }
  end
  ans = m * (1 << (n - 1))
  (1...n).each do |j|
    ones = grid.count { |row| row[j] == 1 }
    ans += [ones, m - ones].max * (1 << (n - 1 - j))
  end
  ans
end
