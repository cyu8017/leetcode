# LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
# https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def min_time(n, edges)
  g = Array.new(n) { [] }
  edges.each { |e| g[e[0]] << [e[1], e[2], e[3]] }
  inf = 10**18
  dist = Array.new(n, inf)
  dist[0] = 0
  pq = [[0, 0]]
  push = lambda do |t, u|
    lo = 0
    hi = pq.length
    while lo < hi
      mid = (lo + hi) >> 1
      if pq[mid][0] < t
        lo = mid + 1
      else
        hi = mid
      end
    end
    pq.insert(lo, [t, u])
  end
  until pq.empty?
    t, u = pq.shift
    next if t != dist[u]
    return t if u == n - 1
    g[u].each do |to, start, last|
      nt = t
      next if nt > last
      nt = start if nt < start
      nt += 1
      if nt < dist[to]
        dist[to] = nt
        push.call(nt, to)
      end
    end
  end
  dist[n - 1] == inf ? -1 : dist[n - 1]
end
