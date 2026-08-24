# LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
# https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

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
# @param {Integer} start
# @param {Integer} k
# @return {Integer}
def count_within(g, start, k)
  return 0 if k < 0

  n = g.length
  vis = Array.new(n, false)
  q = [[start, 0]]
  vis[start] = true
  cnt = 0
  qi = 0
  while qi < q.length
    u, d = q[qi]
    qi += 1
    cnt += 1
    next if d == k

    g[u].each do |v|
      unless vis[v]
        vis[v] = true
        q << [v, d + 1]
      end
    end
  end
  cnt
end

# @param {Integer[][]} edges1
# @param {Integer[][]} edges2
# @param {Integer} k
# @return {Integer[]}
def max_target_nodes(edges1, edges2, k)
  n = edges1.length + 1
  m = edges2.length + 1
  g1 = build_tree(n, edges1)
  g2 = build_tree(m, edges2)
  cnt1 = n.times.map { |i| count_within(g1, i, k) }
  best2 = 0
  if k > 0
    m.times do |i|
      c = count_within(g2, i, k - 1)
      best2 = c if c > best2
    end
  end
  n.times.map { |i| cnt1[i] + best2 }
end
