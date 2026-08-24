# LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
# https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} target
# @param {Integer} k
# @return {Integer}
def min_threshold(n, edges, source, target, k)
  can = lambda do |threshold|
    inf = 1_000_000_000
    dist = Array.new(n, inf)
    dist[source] = 0
    dq = [source]
    until dq.empty?
      u = dq.shift
      g[u].each do |to, weight|
        cost = weight > threshold ? 1 : 0
        next if dist[u] + cost >= dist[to] || dist[u] + cost > k
        dist[to] = dist[u] + cost
        if cost == 0
          dq.unshift(to)
        else
          dq << to
        end
      end
    end
    dist[target] <= k
  end
  return 0 if source == target
  g = Array.new(n) { [] }
  max_weight = 0
  edges.each do |e|
    g[e[0]] << [e[1], e[2]]
    g[e[1]] << [e[0], e[2]]
    max_weight = e[2] if e[2] > max_weight
  end
  return -1 unless can.call(max_weight)
  lo = 0
  hi = max_weight
  while lo < hi
    mid = lo + (hi - lo) / 2
    if can.call(mid)
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
