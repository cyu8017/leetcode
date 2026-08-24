# LeetCode 0864 - Shortest Path to Get All Keys
# https://leetcode.com/problems/shortest-path-to-get-all-keys/

# @param {String[]} grid
# @return {Integer}
def shortest_path_all_keys(grid)
  m = grid.length
  n = grid[0].length
  all_keys = 0
  start = [0, 0]
  m.times do |i|
    n.times do |j|
      if grid[i][j] == "@"
        start = [i, j]
      elsif grid[i][j] >= "a" && grid[i][j] <= "f"
        all_keys |= 1 << (grid[i][j].ord - 97)
      end
    end
  end

  queue = [[start[0], start[1], 0, 0]]
  seen = { [start[0], start[1], 0] => true }
  until queue.empty?
    r, c, mask, dist = queue.shift
    return dist if mask == all_keys

    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      next unless nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != "#"

      cell = grid[nr][nc]
      nmask = mask
      nmask |= 1 << (cell.ord - 97) if cell >= "a" && cell <= "f"
      next if cell >= "A" && cell <= "F" && (mask & (1 << (cell.ord - 65))).zero?

      state = [nr, nc, nmask]
      next if seen[state]

      seen[state] = true
      queue << [nr, nc, nmask, dist + 1]
    end
  end
  -1
end
