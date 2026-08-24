# LeetCode 2699 - Modify Graph Edge Weights
# https://leetcode.com/problems/modify-graph-edge-weights/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} source
# @param {Integer} destination
# @param {Integer} target
# @return {Integer[][]}
def modified_graph_edges(n, edges, source, destination, target)
  inf = 2_000_000_000
  dijkstra = lambda do |ignore_neg|
    dist = Array.new(n, inf)
    dist[source] = 0
    pq = [[0, source]]
    until pq.empty?
      pq.sort_by! { |x| x[0] }
      d, u = pq.shift
      next if d != dist[u]

      edges.each do |e|
        a, b, w = e[0], e[1], e[2]
        next if a != u && b != u

        to = a == u ? b : a
        if w == -1
          next if ignore_neg

          w = 1
        end
        if d + w < dist[to]
          dist[to] = d + w
          pq << [dist[to], to]
        end
      end
    end
    dist
  end
  d = dijkstra.call(true)
  return [] if d[destination] < target

  matched = d[destination] == target
  edges.each_index do |i|
    next if edges[i][2] != -1

    if matched
      edges[i][2] = inf
      next
    end
    edges[i][2] = 1
    d = dijkstra.call(false)
    if d[destination] <= target
      edges[i][2] += target - d[destination]
      matched = true
    end
  end
  d = dijkstra.call(false)
  return [] if d[destination] != target

  edges
end
