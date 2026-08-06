# LeetCode 1443 - Minimum Time To Collect All Apples In A Tree
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

def min_time(n, edges, has_apple)
  graph = Array.new(n) { [] }
  edges.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  visit = lambda do |node, parent|
    cost = 0
    graph[node].each do |child|
      next if child == parent
      child_cost = visit.call(child, node)
      cost += child_cost + 2 if child_cost > 0 || has_apple[child]
    end
    cost
  end
  visit.call(0, -1)
end
