# LeetCode 2662 - Minimum Cost of a Path With Special Roads
# https://leetcode.com/problems/minimum-cost-of-a-path-with-special-roads/

# @param {Integer[]} start
# @param {Integer[]} target
# @param {Integer[][]} special_roads
# @return {Integer}
def minimum_cost(start, target, special_roads)
  points = [start, target]
  special_roads.each do |r|
    points << [r[0], r[1]]
    points << [r[2], r[3]]
  end
  n = points.length
  man = lambda { |a, b| (a[0] - b[0]).abs + (a[1] - b[1]).abs }
  g = Array.new(n) { [] }
  n.times do |i|
    n.times do |j|
      g[i] << [j, man.call(points[i], points[j])] if i != j
    end
  end
  special_roads.each do |r|
    u = v = -1
    points.each_with_index do |p, i|
      u = i if p[0] == r[0] && p[1] == r[1]
      v = i if p[0] == r[2] && p[1] == r[3]
    end
    g[u] << [v, r[4]] if u >= 0 && v >= 0
  end
  dist = Array.new(n, 10**18)
  dist[0] = 0
  pq = [[0, 0]]
  until pq.empty?
    pq.sort_by! { |x| x[0] }
    cost, idx = pq.shift
    next if cost > dist[idx]

    g[idx].each do |to, w|
      if cost + w < dist[to]
        dist[to] = cost + w
        pq << [dist[to], to]
      end
    end
  end
  dist[1]
end
