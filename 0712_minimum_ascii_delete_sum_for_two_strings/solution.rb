# LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

# @param {String} s1
# @param {String} s2
# @return {Integer}
def minimum_delete_sum(s1, s2)
  m = s1.length
  n = s2.length
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each { |i| dp[i][0] = dp[i - 1][0] + s1[i - 1].ord }
  (1..n).each { |j| dp[0][j] = dp[0][j - 1] + s2[j - 1].ord }

  (1..m).each do |i|
    (1..n).each do |j|
      dp[i][j] = if s1[i - 1] == s2[j - 1]
                   dp[i - 1][j - 1]
                 else
                   [dp[i - 1][j] + s1[i - 1].ord, dp[i][j - 1] + s2[j - 1].ord].min
                 end
    end
  end
  dp[m][n]
end
