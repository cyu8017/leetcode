# LeetCode 1771 - Maximize Palindrome Length From Subsequences
# https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

# @param {String} word1
# @param {String} word2
# @return {Integer}
def longest_palindrome(word1, word2)
  s = word1 + word2
  n = s.length
  n1 = word1.length
  dp = Array.new(n) { Array.new(n, 0) }
  ans = 0
  (n - 1).downto(0) do |i|
    dp[i][i] = 1
    (i + 1...n).each do |j|
      if s[i] == s[j]
        dp[i][j] = j == i + 1 ? 2 : dp[i + 1][j - 1] + 2
        ans = [ans, dp[i][j]].max if i < n1 && n1 <= j
      else
        dp[i][j] = [dp[i + 1][j], dp[i][j - 1]].max
      end
    end
  end
  ans
end
