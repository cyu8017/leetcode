# LeetCode 0882 - Reachable Nodes In Subdivided Graph
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

# @param {Integer[][]} edges
# @param {Integer} max_moves
# @param {Integer} n
# @return {Integer}
def reachable_nodes(edges, max_moves, n)
  graph = Hash.new { |h, k| h[k] = {} }
  edges.each do |u, v, cnt|
    graph[u][v] = cnt
    graph[v][u] = cnt
  end
  pq = [[-max_moves, 0]]
  seen = {}
  until pq.empty?
    pq.sort_by! { |moves, _| moves }
    moves, node = pq.shift
    moves = -moves
    next if seen.key?(node)

    seen[node] = moves
    graph[node].each do |nei, cnt|
      remain = moves - cnt - 1
      pq << [-remain, nei] if !seen.key?(nei) && remain >= 0
    end
  end
  ans = seen.length
  edges.each do |u, v, cnt|
    ans += [cnt, (seen[u] || 0) + (seen[v] || 0)].min
  end
  ans
end
