# LeetCode 0994 - Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/

# @param {Integer[][]} grid
# @return {Integer}
def oranges_rotting(grid)
  m = grid.length
  n = grid[0].length
  queue = []
  fresh = 0
  m.times do |i|
    n.times do |j|
      if grid[i][j] == 2
        queue << [i, j]
      elsif grid[i][j] == 1
        fresh += 1
      end
    end
  end
  minutes = 0
  while !queue.empty? && fresh.positive?
    queue.length.times do
      r, c = queue.shift
      [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
        next unless nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1

        grid[nr][nc] = 2
        fresh -= 1
        queue << [nr, nc]
      end
    end
    minutes += 1
  end
  fresh.zero? ? minutes : -1
end
