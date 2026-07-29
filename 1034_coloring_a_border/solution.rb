# LeetCode 1034 - Coloring A Border
# https://leetcode.com/problems/coloring-a-border/

# @param {Integer[][]} grid
# @param {Integer} row
# @param {Integer} col
# @param {Integer} color
# @return {Integer[][]}
def color_border(grid, row, col, color)
  m = grid.length
  n = grid[0].length
  original = grid[row][col]
  component = {}
  stack = [[row, col]]
  component[[row, col]] = true
  until stack.empty?
    r, c = stack.pop
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      next unless nr >= 0 && nr < m && nc >= 0 && nc < n
      next unless grid[nr][nc] == original && !component[[nr, nc]]

      component[[nr, nc]] = true
      stack << [nr, nc]
    end
  end
  border = []
  component.each_key do |r, c|
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      if !(nr >= 0 && nr < m && nc >= 0 && nc < n) || !component[[nr, nc]]
        border << [r, c]
        break
      end
    end
  end
  border.each { |r, c| grid[r][c] = color }
  grid
end
