# LeetCode 0694 - Number of Distinct Islands
# https://leetcode.com/problems/number-of-distinct-islands/

# @param {Integer[][]} grid
# @return {Integer}
def num_distinct_islands(grid)
  return 0 if grid.nil? || grid.empty?

  m = grid.length
  n = grid[0].length
  shapes = {}

  dfs = lambda do |r, c, br, bc, path|
    return if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] == 0

    grid[r][c] = 0
    path << [r - br, c - bc]
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      dfs.call(r + dr, c + dc, br, bc, path)
    end
  end

  m.times do |i|
    n.times do |j|
      next unless grid[i][j] == 1

      path = []
      dfs.call(i, j, i, j, path)
      shapes[path] = true
    end
  end
  shapes.length
end
