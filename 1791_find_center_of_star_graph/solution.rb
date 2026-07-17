# LeetCode 1791 - Find Center of Star Graph
# https://leetcode.com/problems/find-center-of-star-graph/

# @param {Integer[][]} edges
# @return {Integer}
def find_center(edges)
  a, b = edges[0]
  c, d = edges[1]
  (a == c || a == d) ? a : b
end
