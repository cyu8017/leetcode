# LeetCode 3332 - Maximum Points Tourist Can Earn
# https://leetcode.com/problems/maximum-points-tourist-can-earn/

# @param {Integer} n
# @param {Integer} k
# @param {Integer[][]} stay_score
# @param {Integer[][]} travel_score
# @return {Integer}
def max_score(n, k, stay_score, travel_score)
  dp = Array.new(n, 0)
  k.times do |day|
    ndp = Array.new(n, -(1 << 30))
    n.times do |dest|
      best = -(1 << 30)
      n.times do |src|
        val = dp[src]
        val += src == dest ? stay_score[day][dest] : travel_score[src][dest]
        best = val if val > best
      end
      ndp[dest] = best
    end
    dp = ndp
  end
  ans = dp[0]
  (1...n).each { |i| ans = dp[i] if dp[i] > ans }
  ans
end
