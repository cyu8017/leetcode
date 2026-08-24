# LeetCode 2430 - Maximum Deletions on a String
# https://leetcode.com/problems/maximum-deletions-on-a-string/

# @param {String} s
# @return {Integer}
def delete_string(s)
  n = s.length
  lcp = Array.new(n + 1) { Array.new(n + 1, 0) }
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      lcp[i][j] = lcp[i + 1][j + 1] + 1 if s[i] == s[j]
    end
  end
  dp = Array.new(n, 0)
  (n - 1).downto(0) do |i|
    dp[i] = 1
    length = 1
    while i + 2 * length <= n
      dp[i] = [dp[i], 1 + dp[i + length]].max if lcp[i][i + length] >= length
      length += 1
    end
  end
  dp[0]
end
