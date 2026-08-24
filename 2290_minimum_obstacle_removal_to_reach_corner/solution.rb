# LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

# @param {Integer[][]} grid
# @return {Integer}
def minimum_obstacles(grid)
  m = grid.length
  n = grid[0].length
  dist = Array.new(m) { Array.new(n, Float::INFINITY) }
  dist[0][0] = 0
  dq = [[0, 0]]
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  until dq.empty?
    r, c = dq.shift
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next if nr < 0 || nr >= m || nc < 0 || nc >= n

      nd = dist[r][c] + grid[nr][nc]
      next unless nd < dist[nr][nc]

      dist[nr][nc] = nd
      if grid[nr][nc] == 0
        dq.unshift([nr, nc])
      else
        dq << [nr, nc]
      end
    end
  end
  dist[m - 1][n - 1].to_i
end
