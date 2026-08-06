# LeetCode 1230 - Toss Strange Coins
# https://leetcode.com/problems/toss-strange-coins/

# @param {Float[]} prob
# @param {Integer} target
# @return {Float}
def probability_of_heads(prob, target)
  dp = [1.0] + [0.0] * target
  prob.each do |p|
    target.downto(0) do |heads|
      dp[heads] = dp[heads] * (1 - p) + (heads > 0 ? dp[heads - 1] * p : 0)
    end
  end
  dp[target]
end
