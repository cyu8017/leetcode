# LeetCode 3070 - Count Submatrices with Top-Left Element and Sum Less Than k
# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def count_submatrices(grid, k)
  n = grid.length
  m = grid[0].length
  ans = 0
  s = Array.new(n + 1) { Array.new(m + 1, 0) }
  n.times do |i|
    m.times do |j|
      s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + grid[i][j]
      ans += 1 if s[i + 1][j + 1] <= k
    end
  end
  ans
end
