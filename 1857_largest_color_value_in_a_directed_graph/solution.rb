# LeetCode 1857 - Largest Color Value in a Directed Graph
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

# @param {String} colors
# @param {Integer[][]} edges
# @return {Integer}
def largest_path_value(colors, edges)
  n = colors.length
  indegree = Array.new(n, 0)
  adjacency = Array.new(n) { [] }

  edges.each do |from_node, to_node|
    adjacency[from_node] << to_node
    indegree[to_node] += 1
  end

  queue = (0...n).select { |node| indegree[node] == 0 }
  dp = Array.new(n) { Array.new(26, 0) }
  (0...n).each do |node|
    dp[node][colors[node].ord - "a".ord] = 1
  end

  processed = 0
  answer = 0
  qi = 0

  while qi < queue.length
    node = queue[qi]
    qi += 1
    processed += 1
    answer = [answer, dp[node].max].max

    adjacency[node].each do |neighbor|
      neighbor_color = colors[neighbor].ord - "a".ord
      (0...26).each do |color_index|
        candidate = dp[node][color_index]
        candidate += 1 if color_index == neighbor_color
        dp[neighbor][color_index] = candidate if candidate > dp[neighbor][color_index]
      end

      indegree[neighbor] -= 1
      queue << neighbor if indegree[neighbor] == 0
    end
  end

  processed == n ? answer : -1
end
