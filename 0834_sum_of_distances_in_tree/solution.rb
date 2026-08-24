# LeetCode 0834 - Sum of Distances in Tree
# https://leetcode.com/problems/sum-of-distances-in-tree/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def sum_of_distances_in_tree(n, edges)
  graph = Hash.new { |h, k| h[k] = [] }
  edges.each do |a, b|
    graph[a] << b
    graph[b] << a
  end

  count = Array.new(n, 1)
  ans = Array.new(n, 0)

  post = lambda do |node, parent|
    graph[node].each do |child|
      next if child == parent

      post.call(child, node)
      count[node] += count[child]
      ans[node] += ans[child] + count[child]
    end
  end

  reroot = lambda do |node, parent|
    graph[node].each do |child|
      next if child == parent

      ans[child] = ans[node] - count[child] + (n - count[child])
      reroot.call(child, node)
    end
  end

  post.call(0, -1)
  reroot.call(0, -1)
  ans
end
