# LeetCode 1548 - The Most Similar Path in a Graph
# https://leetcode.com/problems/the-most-similar-path-in-a-graph/

# @param {Integer} n
# @param {Integer[][]} roads
# @param {String[]} names
# @param {String[]} target_path
# @return {Integer[]}
def most_similar(n, roads, names, target_path)
  graph = Array.new(n) { [] }
  roads.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  dp = (0...n).map { |node| [(names[node] != target_path[0] ? 1 : 0), [node]] }
  (1...target_path.length).each do |i|
    next_dp = []
    (0...n).each do |node|
      cost, path = graph[node].map { |previous| dp[previous] }.min_by { |c, _| c }
      next_dp << [cost + (names[node] != target_path[i] ? 1 : 0), path + [node]]
    end
    dp = next_dp
  end
  dp.min_by { |c, _| c }[1]
end
