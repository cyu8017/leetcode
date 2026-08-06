# LeetCode 1971 - Find if Path Exists in Graph
# https://leetcode.com/problems/find-if-path-exists-in-graph/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @return {Boolean}
def valid_path(n, edges, source, destination)
  return true if source == destination
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  stack = [source]
  seen = { source => true }
  until stack.empty?
    u = stack.pop
    return true if u == destination
    g[u].each do |v|
      next if seen[v]
      seen[v] = true
      stack << v
    end
  end
  false
end
