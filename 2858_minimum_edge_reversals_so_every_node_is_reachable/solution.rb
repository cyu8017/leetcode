# LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
# https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def min_edge_reversals(n, edges)
  g = Array.new(n) { [] }
  edges.each do |u, v|
    g[u] << [v, 0]
    g[v] << [u, 1]
  end
  ans = Array.new(n, 0)

  dfs1 = lambda do |u, p|
    g[u].each do |v, ww|
      next if v == p

      ans[0] += ww
      dfs1.call(v, u)
    end
  end

  dfs2 = lambda do |u, p|
    g[u].each do |v, ww|
      next if v == p

      ans[v] = ww == 0 ? ans[u] + 1 : ans[u] - 1
      dfs2.call(v, u)
    end
  end

  dfs1.call(0, -1)
  dfs2.call(0, -1)
  ans
end
