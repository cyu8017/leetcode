# LeetCode 0785 - Is Graph Bipartite?
# https://leetcode.com/problems/is-graph-bipartite/

# @param {Integer[][]} graph
# @return {Boolean}
def is_bipartite(graph)
  color = Array.new(graph.length, -1)

  dfs = lambda do |node, c|
    color[node] = c
    graph[node].each do |nei|
      if color[nei] == -1
        return false unless dfs.call(nei, c ^ 1)
      elsif color[nei] == c
        return false
      end
    end
    true
  end

  graph.length.times do |node|
    return false if color[node] == -1 && !dfs.call(node, 0)
  end
  true
end
