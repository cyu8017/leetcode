# LeetCode 1615 - Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/

# @param {Integer} n
# @param {Integer[][]} roads
# @return {Integer}
def maximal_network_rank(n, roads)
  degree = Array.new(n, 0)
  edges = {}
  roads.each do |a, b|
    degree[a] += 1
    degree[b] += 1
    edges[[a, b].minmax] = true
  end
  ans = 0
  (0...n).each do |a|
    ((a + 1)...n).each do |b|
      ans = [ans, degree[a] + degree[b] - (edges[[a, b]] ? 1 : 0)].max
    end
  end
  ans
end
