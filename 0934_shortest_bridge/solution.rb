# LeetCode 0934 - Shortest Bridge
# https://leetcode.com/problems/shortest-bridge/

# @param {Integer[][]} grid
# @return {Integer}
def shortest_bridge(grid)
  n = grid.length
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  sr = sc = 0
  n.times do |i|
    n.times do |j|
      if grid[i][j] == 1
        sr = i
        sc = j
        break
      end
    end
    break if grid[sr][sc] == 1
  end

  dfs = lambda do |r, c|
    return if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1

    grid[r][c] = 2
    dirs.each { |dr, dc| dfs.call(r + dr, c + dc) }
  end
  dfs.call(sr, sc)

  queue = []
  n.times do |i|
    n.times do |j|
      queue << [i, j, 0] if grid[i][j] == 2
    end
  end
  until queue.empty?
    r, c, dist = queue.shift
    dirs.each do |dr, dc|
      nr = r + dr
      nc = c + dc
      next unless nr >= 0 && nr < n && nc >= 0 && nc < n
      return dist if grid[nr][nc] == 1

      if grid[nr][nc] == 0
        grid[nr][nc] = 2
        queue << [nr, nc, dist + 1]
      end
    end
  end
  -1
end
