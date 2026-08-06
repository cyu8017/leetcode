# LeetCode 1143 - Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

# @param {String} text1
# @param {String} text2
# @return {Integer}
def longest_common_subsequence(text1, text2)
  m = text1.length
  n = text2.length
  dp = Array.new(n + 1, 0)
  (1..m).each do |i|
    prev = 0
    (1..n).each do |j|
      cur = dp[j]
      if text1[i - 1] == text2[j - 1]
        dp[j] = prev + 1
      else
        dp[j] = [dp[j], dp[j - 1]].max
      end
      prev = cur
    end
  end
  dp[n]
end
