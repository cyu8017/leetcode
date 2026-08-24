# LeetCode 2374 - Node With Highest Edge Score
# https://leetcode.com/problems/node-with-highest-edge-score/

# @param {Integer[]} edges
# @return {Integer}
def edge_score(edges)
  n = edges.length
  score = Array.new(n, 0)
  (0...n).each { |i| score[edges[i]] += i }
  ans = 0
  (1...n).each { |i| ans = i if score[i] > score[ans] }
  ans
end
