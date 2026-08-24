# LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[][]}
def build_tree(n, edges)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  g
end

# @param {Integer[][]} g
# @param {Integer[]} color
# @return {Integer[]}
def bipartite_count(g, color)
  color.length.times { |i| color[i] = -1 }
  q = [0]
  color[0] = 0
  cnt = [1, 0]
  qi = 0
  while qi < q.length
    u = q[qi]
    qi += 1
    g[u].each do |v|
      if color[v] == -1
        color[v] = color[u] ^ 1
        cnt[color[v]] += 1
        q << v
      end
    end
  end
  cnt
end

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @return {Integer[]}
def max_target_nodes(edges1, edges2)
  n = edges1.length + 1
  m = edges2.length + 1
  g1 = build_tree(n, edges1)
  g2 = build_tree(m, edges2)
  color1 = Array.new(n, 0)
  color2 = Array.new(m, 0)
  c1 = bipartite_count(g1, color1)
  c2 = bipartite_count(g2, color2)
  best2 = [c2[0], c2[1]].max
  n.times.map { |i| c1[color1[i]] + best2 }
end
