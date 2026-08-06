# LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {String} labels
# @return {Integer[]}
def count_sub_trees(n, edges, labels)
  graph = Array.new(n) { [] }
  edges.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  answer = Array.new(n, 0)

  dfs = lambda do |node, parent|
    counts = Array.new(26, 0)
    index = labels[node].ord - 97
    counts[index] = 1
    graph[node].each do |neighbor|
      next if neighbor == parent
      child = dfs.call(neighbor, node)
      26.times { |i| counts[i] += child[i] }
    end
    answer[node] = counts[index]
    counts
  end
  dfs.call(0, -1)
  answer
end
