# LeetCode 3552 - Grid Teleportation Traversal
# https://leetcode.com/problems/grid-teleportation-traversal/

# @param {String[]} matrix
# @return {Integer}
def min_moves(matrix)
  m = matrix.length
  n = matrix[0].length
  g = {}
  (0...m).each do |i|
    (0...n).each do |j|
      c = matrix[i][j]
      if c.match?(/[A-Za-z]/)
        (g[c] ||= []) << [i, j]
      end
    end
  end
  dirs = [-1, 0, 1, 0, -1]
  inf = 1 << 30
  dist = Array.new(m) { Array.new(n, inf) }
  dist[0][0] = 0
  q = [[0, 0]]
  until q.empty?
    i, j = q.shift
    d = dist[i][j]
    return d if i == m - 1 && j == n - 1
    c = matrix[i][j]
    if g.key?(c)
      g[c].each do |x, y|
        if d < dist[x][y]
          dist[x][y] = d
          q.unshift([x, y])
        end
      end
      g.delete(c)
    end
    (0...4).each do |idx|
      x = i + dirs[idx]
      y = j + dirs[idx + 1]
      if x >= 0 && x < m && y >= 0 && y < n && matrix[x][y] != "#" && d + 1 < dist[x][y]
        dist[x][y] = d + 1
        q << [x, y]
      end
    end
  end
  -1
end
