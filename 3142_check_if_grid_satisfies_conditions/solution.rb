# LeetCode 3142 - Check if Grid Satisfies Conditions
# https://leetcode.com/problems/check-if-grid-satisfies-conditions/

# @param {Integer[][]} grid
# @return {Boolean}
def satisfies_conditions(grid)
  m = grid.length
  n = grid[0].length
  m.times do |i|
    n.times do |j|
      x = grid[i][j]
      return false if i + 1 < m && x != grid[i + 1][j]
      return false if j + 1 < n && x == grid[i][j + 1]
    end
  end
  true
end
