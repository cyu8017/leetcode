# LeetCode 1293 - Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

# @param {Integer[][]} grid
# @param {Integer} k
# @return {Integer}
def shortest_path(grid, k)
  m = grid.length
  n = grid[0].length
  return m + n - 2 if k >= m + n - 2
  queue = [[0, 0, k, 0]]
  best = { [0, 0] => k }
  until queue.empty?
    r, c, remaining, distance = queue.shift
    return distance if r == m - 1 && c == n - 1
    [[1, 0], [-1, 0], [0, 1], [0, -1]].each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr.between?(0, m - 1) && nc.between?(0, n - 1)
      nxt = remaining - grid[nr][nc]
      if nxt >= 0 && nxt > best.fetch([nr, nc], -1)
        best[[nr, nc]] = nxt
        queue << [nr, nc, nxt, distance + 1]
      end
    end
  end
  -1
end
