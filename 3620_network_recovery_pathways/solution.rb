# LeetCode 3620 - Network Recovery Pathways
# https://leetcode.com/problems/network-recovery-pathways/

# @param {Integer[][]} edges
# @param {Boolean[]} online
# @param {Integer} k
# @return {Integer}
def find_max_path_score(edges, online, k)
  n = online.length
  g = Array.new(n) { [] }
  l = 2147483647
  r = 0
  edges.each do |e|
    u, v, w = e[0], e[1], e[2]
    next if !online[u] || !online[v]

    g[u] << [v, w]
    l = w if w < l
    r = w if w > r
  end
  return -1 if l == 2147483647

  check = lambda do |mid|
    inf = 1073741823
    dist = Array.new(n, inf)
    dist[0] = 0
    pq = [[0, 0]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      return false if d > k
      return true if u == n - 1
      next if dist[u] < d

      g[u].each do |v, w|
        next if w < mid

        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          pq << [nd, v]
        end
      end
    end
    false
  end

  while l < r
    mid = (l + r + 1) >> 1
    if check.call(mid)
      l = mid
    else
      r = mid - 1
    end
  end
  check.call(l) ? l : -1
end
