# LeetCode 2128 - Remove All Ones With Row and Column Flips
# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

# @param {Integer[][]} grid
# @return {Boolean}
def remove_ones(grid)
  m = grid.length
  n = grid[0].length
  (1...m).each do |i|
    same = grid[i][0] == grid[0][0]
    n.times do |j|
      return false if (grid[i][j] == grid[0][j]) != same
    end
  end
  true
end
