# LeetCode 0064 - Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

# @param {Integer[][]} grid
# @return {Integer}
def min_path_sum(grid)
  rows = grid.length
  cols = grid[0].length

  rows.times do |i|
    cols.times do |j|
      next if i.zero? && j.zero?

      if i.zero?
        grid[i][j] += grid[i][j - 1]
      elsif j.zero?
        grid[i][j] += grid[i - 1][j]
      else
        grid[i][j] += [grid[i - 1][j], grid[i][j - 1]].min
      end
    end
  end

  grid[rows - 1][cols - 1]
end
