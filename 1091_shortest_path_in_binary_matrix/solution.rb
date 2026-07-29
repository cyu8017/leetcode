# LeetCode 1091 - Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# @param {Integer[][]} grid
# @return {Integer}
def shortest_path_binary_matrix(grid)
  n = grid.length
  return -1 if grid[0][0] != 0 || grid[n - 1][n - 1] != 0

  queue = [[0, 0, 1]]
  grid[0][0] = 1
  until queue.empty?
    r, c, dist = queue.shift
    return dist if r == n - 1 && c == n - 1

    (-1..1).each do |dr|
      (-1..1).each do |dc|
        next if dr.zero? && dc.zero?

        nr = r + dr
        nc = c + dc
        next unless nr.between?(0, n - 1) && nc.between?(0, n - 1) && grid[nr][nc].zero?

        grid[nr][nc] = 1
        queue << [nr, nc, dist + 1]
      end
    end
  end
  -1
end
