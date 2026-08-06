# LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# @param {Integer} n
# @param {Integer[][]} edges
# @return {Integer[]}
def find_smallest_set_of_vertices(n, edges)
  incoming = {}
  edges.each { |_, v| incoming[v] = true }
  (0...n).reject { |v| incoming[v] }
end
