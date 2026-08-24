# LeetCode 2368 - Reachable Nodes With Restrictions
# https://leetcode.com/problems/reachable-nodes-with-restrictions/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} restricted
# @return {Integer}
def reachable_nodes(n, edges, restricted)
  ban = {}
  restricted.each { |x| ban[x] = true }
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0
  vis = Array.new(n, false)
  q = [0]
  vis[0] = true
  until q.empty?
    u = q.shift
    ans += 1
    g[u].each do |v|
      if !vis[v] && !ban.key?(v)
        vis[v] = true
        q << v
      end
    end
  end
  ans
end
