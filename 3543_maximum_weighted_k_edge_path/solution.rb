# LeetCode 3543 - Maximum Weighted K-Edge Path
# https://leetcode.com/problems/maximum-weighted-k-edge-path/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer} k
# @param {Integer} t
# @return {Integer}
def max_weight(n, edges, k, t)
  graph = Array.new(n) { [] }
  edges.each { |e| graph[e[0]] << [e[1], e[2]] }
  dp = Array.new(n) { Array.new(k + 1) { {} } }
  (0...n).each { |u| dp[u][0][0] = true }
  (0...k).each do |i|
    (0...n).each do |u|
      dp[u][i].each_key do |sm|
        graph[u].each do |to, w|
          ns = sm + w
          dp[to][i + 1][ns] = true if ns < t
        end
      end
    end
  end
  ans = -1
  (0...n).each do |u|
    dp[u][k].each_key { |sm| ans = sm if sm > ans }
  end
  ans
end
