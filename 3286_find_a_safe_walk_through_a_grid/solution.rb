# LeetCode 3286 - Find a Safe Walk Through a Grid
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

# @param {Integer[][]} grid
# @param {Integer} health
# @return {Boolean}
def find_safe_walk(grid, health)
  m = grid.length
  n = grid[0].length
  vis = Array.new(m) { Array.new(n, -1) }
  qh = health - grid[0][0]
  return false if qh <= 0

  q = [[0, 0, qh]]
  vis[0][0] = qh
  dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
  until q.empty?
    cur = q.shift
    return true if cur[0] == m - 1 && cur[1] == n - 1

    dirs.each do |d|
      nr = cur[0] + d[0]
      nc = cur[1] + d[1]
      next if nr < 0 || nc < 0 || nr >= m || nc >= n

      nh = cur[2] - grid[nr][nc]
      next if nh <= 0

      if nh > vis[nr][nc]
        vis[nr][nc] = nh
        q << [nr, nc, nh]
      end
    end
  end
  false
end
