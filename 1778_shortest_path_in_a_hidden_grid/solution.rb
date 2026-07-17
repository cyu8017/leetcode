# LeetCode 1778 - Shortest Path in a Hidden Grid
# https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

# @param {Integer[][]} grid
# @return {Integer}
def find_shortest_path(grid)
  dir = { 'U' => [-1, 0], 'D' => [1, 0], 'L' => [0, -1], 'R' => [0, 1] }
  opp = { 'U' => 'D', 'D' => 'U', 'L' => 'R', 'R' => 'L' }
  m = grid.length
  n = grid[0].length
  r = 0
  c = 0
  (0...m).each do |i|
    (0...n).each do |j|
      if grid[i][j] == -1
        r = i
        c = j
      end
    end
  end

  can_move = lambda do |d|
    nr = r + dir[d][0]
    nc = c + dir[d][1]
    nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0
  end
  move = lambda do |d|
    if can_move.call(d)
      r += dir[d][0]
      c += dir[d][1]
    end
  end
  is_target = -> { grid[r][c] == 2 }

  world = { [0, 0] => 1 }
  target = nil
  return 0 if is_target.call

  dfs = lambda do |cr, cc|
    dir.each do |d, (dr, dc)|
      next unless can_move.call(d)

      move.call(d)
      nr = cr + dr
      nc = cc + dc
      unless world.key?([nr, nc])
        world[[nr, nc]] = is_target.call ? 2 : 1
        target = [nr, nc] if is_target.call
        dfs.call(nr, nc)
      end
      move.call(opp[d])
    end
  end

  dfs.call(0, 0)
  return -1 if target.nil?

  queue = [[0, 0, 0]]
  seen = { [0, 0] => true }
  until queue.empty?
    cr, cc, dist = queue.shift
    return dist if [cr, cc] == target

    dir.each_value do |(dr, dc)|
      nxt = [cr + dr, cc + dc]
      if world.key?(nxt) && !seen.key?(nxt)
        seen[nxt] = true
        queue << [nxt[0], nxt[1], dist + 1]
      end
    end
  end
  -1
end
