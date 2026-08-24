# LeetCode 3710 - Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/

# @param {Integer[][]} points
# @return {Integer}
def max_partition_factor(points)
  n = points.length
  return 0 if n == 2

  dist = lambda do |i, j|
    (points[i][0] - points[j][0]).abs + (points[i][1] - points[j][1]).abs
  end
  ok = lambda do |d|
    g = Array.new(n) { [] }
    (0...n).each do |i|
      ((i + 1)...n).each do |j|
        if dist.call(i, j) < d
          g[i] << j
          g[j] << i
        end
      end
    end
    color = Array.new(n, -1)
    (0...n).each do |i|
      next if color[i] != -1

      q = [i]
      color[i] = 0
      until q.empty?
        u = q.shift
        g[u].each do |v|
          if color[v] == -1
            color[v] = color[u] ^ 1
            q << v
          elsif color[v] == color[u]
            return false
          end
        end
      end
    end
    true
  end
  lo = 0
  hi = 0
  (0...n).each do |i|
    ((i + 1)...n).each do |j|
      d = dist.call(i, j)
      hi = d if d > hi
    end
  end
  while lo < hi
    mid = (lo + hi + 1) / 2
    if ok.call(mid)
      lo = mid
    else
      hi = mid - 1
    end
  end
  lo
end
