# LeetCode 1042 - Flower Planting With No Adjacent
# https://leetcode.com/problems/flower-planting-with-no-adjacent/

# @param {Integer} n
# @param {Integer[][]} paths
# @return {Integer[]}
def garden_no_adj(n, paths)
  graph = Hash.new { |h, k| h[k] = [] }
  paths.each do |a, b|
    graph[a] << b
    graph[b] << a
  end
  ans = Array.new(n + 1, 0)
  (1..n).each do |garden|
    used = {}
    graph[garden].each { |nei| used[ans[nei]] = true }
    ans[garden] = (1..4).find { |c| !used[c] }
  end
  ans[1..]
end
