# LeetCode 2642 - Design Graph With Shortest Path Calculator
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph
  def initialize(n, edges)
    @g = Array.new(n) { [] }
    edges.each { |e| @g[e[0]] << [e[1], e[2]] }
  end

  def add_edge(edge)
    @g[edge[0]] << [edge[1], edge[2]]
    nil
  end

  def shortest_path(node1, node2)
    n = @g.length
    dist = Array.new(n, 1 << 30)
    dist[node1] = 0
    pq = [[0, node1]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      return d if u == node2
      next if d > dist[u]

      @g[u].each do |v, w|
        nd = d + w
        if nd < dist[v]
          dist[v] = nd
          pq << [nd, v]
        end
      end
    end
    -1
  end
end
