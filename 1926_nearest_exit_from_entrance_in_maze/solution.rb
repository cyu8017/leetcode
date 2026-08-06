# LeetCode 1926 - Nearest Exit from Entrance in Maze
# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

# @param {Character[][]} maze
# @param {Integer[]} entrance
# @return {Integer}
def nearest_exit(maze, entrance)
  m = maze.length
  n = maze[0].length
  er, ec = entrance
  q = [[er, ec, 0]]
  maze[er][ec] = "+"
  qi = 0
  while qi < q.length
    r, c, d = q[qi]
    qi += 1
    [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]].each do |nr, nc|
      next unless nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == "."
      return d + 1 if nr.zero? || nr == m - 1 || nc.zero? || nc == n - 1
      maze[nr][nc] = "+"
      q << [nr, nc, d + 1]
    end
  end
  -1
end
