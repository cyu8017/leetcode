# LeetCode 2876 - Count Visited Nodes in a Directed Graph
# https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

# @param {Integer[]} edges
# @return {Integer[]}
def count_visited_nodes(edges)
  n = edges.length
  ans = Array.new(n, 0)
  state = Array.new(n, 0)
  stack = []

  dfs = lambda do |u|
    state[u] = 1
    stack << u
    v = edges[u]
    if state[v] == 0
      dfs.call(v)
    elsif state[v] == 1
      idx = stack.length - 1
      idx -= 1 while stack[idx] != v
      cyc = stack.length - idx
      (idx...stack.length).each { |i| ans[stack[i]] = cyc }
    end
    ans[u] = ans[edges[u]] + 1 if ans[u] == 0
    state[u] = 2
    stack.pop
  end

  (0...n).each { |i| dfs.call(i) if state[i] == 0 }
  ans
end
