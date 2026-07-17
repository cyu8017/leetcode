# LeetCode 1719 - Number Of Ways To Reconstruct A Tree
# https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

require 'set'

# @param {Integer[][]} pairs
# @return {Integer}
def check_ways(pairs)
  graph = Hash.new { |hash, key| hash[key] = Set.new }
  pairs.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  nodes = graph.keys
  n = nodes.length
  root = nodes.find { |node| graph[node].size == n - 1 }
  return 0 if root.nil?
  ans = 1
  nodes.each do |node|
    next if node == root
    parent = nil
    parent_degree = n + 1
    graph[node].each do |nei|
      if graph[nei].size >= graph[node].size && graph[nei].size < parent_degree
        parent = nei
        parent_degree = graph[nei].size
      end
    end
    return 0 if parent.nil?
    graph[node].each do |nei|
      return 0 if nei != parent && !graph[parent].include?(nei)
    end
    ans = 2 if graph[parent].size == graph[node].size
  end
  ans
end
