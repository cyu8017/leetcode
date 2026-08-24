# LeetCode 2685 - Count the Number of Complete Components
# https://leetcode.com/problems/count-the-number-of-complete-components/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer}
def count_complete_components(n, edges)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  vis = Array.new(n, false)
  ans = 0
  dfs = nil
  dfs = lambda do |u, nodes|
    vis[u] = true
    nodes << u
    g[u].each { |v| dfs.call(v, nodes) unless vis[v] }
  end
  n.times do |i|
    next if vis[i]

    nodes = []
    dfs.call(i, nodes)
    ecount = 0
    nodes.each { |u| ecount += g[u].length }
    ecount /= 2
    sz = nodes.length
    ans += 1 if ecount == sz * (sz - 1) / 2
  end
  ans
end
