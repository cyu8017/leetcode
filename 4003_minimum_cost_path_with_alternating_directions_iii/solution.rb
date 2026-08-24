# LeetCode 4003 - Minimum Cost Path with Alternating Directions III
# https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-iii/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} penalty
# @return {Integer}
def min_cost(m, n, penalty)
  inf = 2**60
  dist = Array.new(m) { Array.new(n) { [inf, inf] } }
  dist[0][0][1] = 1
  pq = [[1, 0, 0, 1]]
  dirs = [[-1, 0], [0, 1], [0, -1], [1, 0]]
  until pq.empty?
    pq.sort_by! { |a| a[0] }
    d, i, j, k = pq.shift
    return d if i == m - 1 && j == n - 1
    next if d > dist[i][j][k]
    p = penalty[i][j]
    nd = d + p
    if nd < dist[i][j][k ^ 1]
      dist[i][j][k ^ 1] = nd
      pq << [nd, i, j, k ^ 1]
    end
    4.times do |idx|
      x = i + dirs[idx][0]
      y = j + dirs[idx][1]
      next unless x >= 0 && x < m && y >= 0 && y < n
      nd = d + ((x + 1) * (y + 1) + (((idx & 1) ^ k) * p))
      if nd < dist[x][y][k ^ 1]
        dist[x][y][k ^ 1] = nd
        pq << [nd, x, y, k ^ 1]
      end
    end
  end
  -1
end
