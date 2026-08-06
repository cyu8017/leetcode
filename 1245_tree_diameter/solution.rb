# LeetCode 1245 - Tree Diameter
# https://leetcode.com/problems/tree-diameter/

require "set"

# @param {Integer[][]} edges
# @return {Integer}
def tree_diameter(edges)
  return 0 if edges.empty?
  graph = Hash.new { |h, k| h[k] = [] }
  edges.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  farthest = lambda do |start|
    q = [[start, 0]]
    seen = Set[start]
    last = [start, 0]
    until q.empty?
      last = q.shift
      graph[last[0]].each do |v|
        next if seen.include?(v)
        seen.add(v)
        q << [v, last[1] + 1]
      end
    end
    last
  end
  endpoint, = farthest.call(edges[0][0])
  farthest.call(endpoint)[1]
end
