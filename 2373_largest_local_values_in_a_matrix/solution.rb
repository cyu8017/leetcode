# LeetCode 2373 - Largest Local Values in a Matrix
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

# @param {Integer[][]} grid
# @return {Integer[][]}
def largest_local(grid)
  n = grid.length
  ans = Array.new(n - 2) { Array.new(n - 2, 0) }
  (0...n - 2).each do |i|
    (0...n - 2).each do |j|
      mx = 0
      (i...i + 3).each do |r|
        (j...j + 3).each { |c| mx = grid[r][c] if grid[r][c] > mx }
      end
      ans[i][j] = mx
    end
  end
  ans
end
