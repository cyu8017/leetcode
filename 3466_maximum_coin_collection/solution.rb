# LeetCode 3466 - Maximum Coin Collection
# https://leetcode.com/problems/maximum-coin-collection/

# @param {Integer[]} lane1
# @param {Integer[]} lane2
# @return {Integer}
def max_coins(lane1, lane2)
  n = lane1.length
  neg = -(10**18)
  dp = [[lane1[0], neg], [lane2[0], neg]]
  ans = [dp[0][0], dp[1][0]].max
  (1...n).each do |i|
    ndp = [[0, 0], [0, 0]]
    ndp[0][0] = [dp[0][0], 0].max + lane1[i]
    ndp[1][0] = [dp[1][0], 0].max + lane2[i]
    ndp[0][1] = [dp[0][1], dp[1][0]].max + lane1[i]
    ndp[1][1] = [dp[1][1], dp[0][0]].max + lane2[i]
    ndp[0][0] = lane1[i] if lane1[i] > ndp[0][0]
    ndp[1][0] = lane2[i] if lane2[i] > ndp[1][0]
    (0...2).each do |a|
      (0...2).each do |b|
        dp[a][b] = ndp[a][b]
        ans = dp[a][b] if dp[a][b] > ans
      end
    end
  end
  ans
end
