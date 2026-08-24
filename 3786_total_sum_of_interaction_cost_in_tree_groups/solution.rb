# LeetCode 3786 - Total Sum of Interaction Cost in Tree Groups
# https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} group
# @return {Integer}
def interaction_cost(n, edges, group)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  total = Array.new(21, 0)
  group.each { |x| total[x] += 1 }
  parent = Array.new(n, -2)
  parent[0] = -1
  order = [0]
  i = 0
  while i < order.length
    u = order[i]
    g[u].each do |v|
      if parent[v] == -2
        parent[v] = u
        order << v
      end
    end
    i += 1
  end
  count = Array.new(n) { Array.new(21, 0) }
  ans = 0
  (n - 1).downto(0) do |i|
    u = order[i]
    count[u][group[u]] += 1
    g[u].each do |v|
      next unless parent[v] == u
      (1...21).each do |c|
        x = count[v][c]
        ans += x * (total[c] - x)
        count[u][c] += x
      end
    end
  end
  ans
end
