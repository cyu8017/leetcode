# LeetCode 0463 - Island Perimeter
# https://leetcode.com/problems/island-perimeter/

class Solution
  def island_perimeter(grid)
    rows = grid.length
    cols = grid[0].length
    perimeter = 0

    rows.times do |row|
      cols.times do |col|
        next if grid[row][col].zero?

        perimeter += 4
        perimeter -= 2 if row.positive? && grid[row - 1][col] == 1
        perimeter -= 2 if col.positive? && grid[row][col - 1] == 1
      end
    end

    perimeter
  end

  alias_method :islandPerimeter, :island_perimeter
end
