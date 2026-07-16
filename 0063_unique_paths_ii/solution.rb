# LeetCode 0063 - Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

# @param {Integer[][]} obstacle_grid
# @return {Integer}
def unique_paths_with_obstacles(obstacle_grid)
  return 0 if obstacle_grid[0][0] == 1

  rows = obstacle_grid.length
  cols = obstacle_grid[0].length
  row = Array.new(cols, 0)
  row[0] = 1

  rows.times do |i|
    row[0] = 0 if obstacle_grid[i][0] == 1

    (1...cols).each do |j|
      if obstacle_grid[i][j] == 1
        row[j] = 0
      else
        row[j] += row[j - 1]
      end
    end
  end

  row[cols - 1]
end
