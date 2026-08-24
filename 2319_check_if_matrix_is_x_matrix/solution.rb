# LeetCode 2319 - Check if Matrix Is X-Matrix
# https://leetcode.com/problems/check-if-matrix-is-x-matrix/

# @param {Integer[][]} grid
# @return {Boolean}
def check_x_matrix(grid)
  n = grid.length
  (0...n).each do |i|
    (0...n).each do |j|
      diag = i == j || i + j == n - 1
      if diag
        return false if grid[i][j] == 0
      elsif grid[i][j] != 0
        return false
      end
    end
  end
  true
end
