# LeetCode 1514 - Path with Maximum Probability
# https://leetcode.com/problems/path-with-maximum-probability/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Float[]} succ_prob
# @param {Integer} start_node
# @param {Integer} end_node
# @return {Float}
def max_probability(n, edges, succ_prob, start_node, end_node)
  graph = Array.new(n) { [] }
  edges.each_with_index do |(a, b), i|
    probability = succ_prob[i]
    graph[a] << [b, probability]
    graph[b] << [a, probability]
  end
  heap = [[-1.0, start_node]]
  best = Array.new(n, 0.0)
  best[start_node] = 1.0
  until heap.empty?
    heap.sort_by! { |p, _| p }
    probability, node = heap.shift
    probability = -probability
    return probability if node == end_node
    next if probability < best[node]
    graph[node].each do |neighbor, edge_probability|
      candidate = probability * edge_probability
      if candidate > best[neighbor]
        best[neighbor] = candidate
        heap << [-candidate, neighbor]
      end
    end
  end
  0.0
end
