# LeetCode 2204 - Distance to a Cycle in Undirected Graph
# https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def distance_to_cycle(n, edges)
  g = Array.new(n) { [] }
  deg = Array.new(n, 0)
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
    deg[e[0]] += 1
    deg[e[1]] += 1
  end
  q = []
  n.times { |i| q << i if deg[i] == 1 }
  on_cycle = Array.new(n, true)
  until q.empty?
    u = q.shift
    on_cycle[u] = false
    g[u].each do |v|
      deg[v] -= 1
      q << v if deg[v] == 1
    end
  end
  ans = Array.new(n, -1)
  qq = []
  n.times do |i|
    if on_cycle[i]
      ans[i] = 0
      qq << i
    end
  end
  until qq.empty?
    u = qq.shift
    g[u].each do |v|
      if ans[v] == -1
        ans[v] = ans[u] + 1
        qq << v
      end
    end
  end
  ans
end

alias solve distance_to_cycle
