# LeetCode 3419 - Minimize the Maximum Edge Weight of Graph
# https://leetcode.com/problems/minimize-the-maximum-edge-weight-of-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} threshold
# @return {Integer}
def min_max_weight(n, edges, _threshold)
  ok = lambda do |mid|
    g = Array.new(n) { [] }
    edges.each { |e| g[e[1]] << e[0] if e[2] <= mid }
    vis = Array.new(n, false)
    q = [0]
    vis[0] = true
    cnt = 1
    until q.empty?
      u = q.shift
      g[u].each do |v|
        next if vis[v]

        vis[v] = true
        cnt += 1
        q << v
      end
    end
    cnt == n
  end
  lo = 1
  hi = 1_000_001
  ans = -1
  while lo < hi
    mid = (lo + hi) / 2
    if ok.call(mid)
      ans = mid
      hi = mid
    else
      lo = mid + 1
    end
  end
  ans
end
