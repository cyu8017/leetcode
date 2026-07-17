# LeetCode 1765 - Map of Highest Peak
# https://leetcode.com/problems/map-of-highest-peak/

# @param {Integer[][]} is_water
# @return {Integer[][]}
def highest_peak(is_water)
  m = is_water.length
  n = is_water[0].length
  dist = Array.new(m) { Array.new(n, -1) }
  queue = []
  (0...m).each do |i|
    (0...n).each do |j|
      if is_water[i][j] == 1
        dist[i][j] = 0
        queue << [i, j]
      end
    end
  end
  dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  head = 0
  while head < queue.length
    i, j = queue[head]
    head += 1
    dirs.each do |di, dj|
      x = i + di
      y = j + dj
      if x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1
        dist[x][y] = dist[i][j] + 1
        queue << [x, y]
      end
    end
  end
  dist
end
