# LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
# https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

# @param {String[][]} land
# @return {Integer}
def minimum_seconds(land)
  m = land.length
  n = land[0].length
  inf = 10**9
  water = Array.new(m) { Array.new(n, inf) }
  wq = []
  sx = sy = dx = dy = 0
  (0...m).each do |i|
    (0...n).each do |j|
      cell = land[i][j]
      if cell == "*"
        water[i][j] = 0
        wq << [i, j]
      elsif cell == "S"
        sx = i
        sy = j
      elsif cell == "D"
        dx = i
        dy = j
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  h = 0
  while h < wq.length
    x, y = wq[h]
    h += 1
    dirs.each do |ddx, ddy|
      ni = x + ddx
      nj = y + ddy
      next if ni < 0 || nj < 0 || ni >= m || nj >= n
      cell = land[ni][nj]
      next if cell == "X" || cell == "D"
      if water[ni][nj] > water[x][y] + 1
        water[ni][nj] = water[x][y] + 1
        wq << [ni, nj]
      end
    end
  end
  dist = Array.new(m) { Array.new(n, -1) }
  q = [[sx, sy]]
  dist[sx][sy] = 0
  h = 0
  while h < q.length
    x, y = q[h]
    h += 1
    return dist[x][y] if x == dx && y == dy
    dirs.each do |ddx, ddy|
      ni = x + ddx
      nj = y + ddy
      next if ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1
      next if land[ni][nj] == "X"
      nd = dist[x][y] + 1
      next if land[ni][nj] != "D" && nd >= water[ni][nj]
      dist[ni][nj] = nd
      q << [ni, nj]
    end
  end
  -1
end
