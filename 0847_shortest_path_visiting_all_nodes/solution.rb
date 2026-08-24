# LeetCode 0847 - Shortest Path Visiting All Nodes
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/

# @param {Integer[][]} graph
# @return {Integer}
def shortest_path_length(graph)
  n = graph.length
  target = (1 << n) - 1
  queue = (0...n).map { |i| [i, 1 << i, 0] }
  seen = {}
  n.times { |i| seen[[i, 1 << i]] = true }
  until queue.empty?
    node, mask, dist = queue.shift
    return dist if mask == target

    graph[node].each do |nxt|
      nmask = mask | (1 << nxt)
      state = [nxt, nmask]
      next if seen[state]

      seen[state] = true
      queue << [nxt, nmask, dist + 1]
    end
  end
  -1
end
