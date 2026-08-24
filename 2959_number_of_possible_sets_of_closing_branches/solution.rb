# LeetCode 2959 - Number of Possible Sets of Closing Branches
# https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

# @param {Integer} n
# @param {Integer} max_distance
# @param {Integer[][]} roads
# @return {Integer}
def number_of_sets(n, max_distance, roads)
  ans = 0
  (1 << n).times do |mask|
    dist = Array.new(n) { Array.new(n, 1 << 29) }
    n.times { |i| dist[i][i] = 0 }
    roads.each do |u, v, w|
      if (mask & (1 << u)) != 0 && (mask & (1 << v)) != 0 && w < dist[u][v]
        dist[u][v] = w
        dist[v][u] = w
      end
    end
    n.times do |k|
      next if (mask & (1 << k)) == 0

      n.times do |i|
        next if (mask & (1 << i)) == 0

        n.times do |j|
          next if (mask & (1 << j)) == 0

          dist[i][j] = dist[i][k] + dist[k][j] if dist[i][k] + dist[k][j] < dist[i][j]
        end
      end
    end
    ok = true
    i = 0
    while i < n && ok
      if (mask & (1 << i)) == 0
        i += 1
        next
      end
      n.times do |j|
        next if (mask & (1 << j)) == 0

        if dist[i][j] > max_distance
          ok = false
          break
        end
      end
      i += 1
    end
    ans += 1 if ok
  end
  ans
end
