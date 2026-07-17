# LeetCode 1730 - Shortest Path to Get Food
# https://leetcode.com/problems/shortest-path-to-get-food/

# @param {String[][]} grid
# @return {Integer}
def get_food(grid)
  rows = grid.length
  cols = grid[0].length
  queue = []
  seen = Array.new(rows) { Array.new(cols, false) }
  (0...rows).each do |r|
    (0...cols).each do |c|
      if grid[r][c] == '*'
        queue << [r, c, 0]
        seen[r][c] = true
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  head = 0
  while head < queue.length
    r, c, d = queue[head]
    head += 1
    return d if grid[r][c] == '#'
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      if nr >= 0 && nr < rows && nc >= 0 && nc < cols && !seen[nr][nc] && grid[nr][nc] != 'X'
        seen[nr][nc] = true
        queue << [nr, nc, d + 1]
      end
    end
  end
  -1
end
