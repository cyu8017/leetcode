# LeetCode 3290 - Maximum Multiplication Score
# https://leetcode.com/problems/maximum-multiplication-score/

# @param {Integer[]} a
# @param {Integer[]} b
# @return {Integer}
def max_score(a, b)
  neg = -(1 << 62)
  dp = [0, neg, neg, neg, neg]
  b.each do |x|
    4.downto(1) do |k|
      next if dp[k - 1] == neg

      v = dp[k - 1] + a[k - 1] * x
      dp[k] = v if v > dp[k]
    end
  end
  dp[4]
end
