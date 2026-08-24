# LeetCode 0583 - Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def min_distance(word1, word2)
  m = word1.length
  n = word2.length
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  (1..m).each do |i|
    (1..n).each do |j|
      dp[i][j] = if word1[i - 1] == word2[j - 1]
                   dp[i - 1][j - 1] + 1
                 else
                   [dp[i - 1][j], dp[i][j - 1]].max
                 end
    end
  end
  m + n - 2 * dp[m][n]
end
