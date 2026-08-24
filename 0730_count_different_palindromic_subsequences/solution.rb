# LeetCode 0730 - Count Different Palindromic Subsequences
# https://leetcode.com/problems/count-different-palindromic-subsequences/

# @param {String} s
# @return {Integer}
def count_palindromic_subsequences(s)
  mod = 10**9 + 7
  n = s.length
  dp = Array.new(n) { Array.new(n, 0) }
  n.times { |i| dp[i][i] = 1 }

  (2..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      if s[i] != s[j]
        dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
      else
        left = i + 1
        right = j - 1
        left += 1 while left <= right && s[left] != s[i]
        right -= 1 while left <= right && s[right] != s[i]
        if left > right
          dp[i][j] = dp[i + 1][j - 1] * 2 + 2
        elsif left == right
          dp[i][j] = dp[i + 1][j - 1] * 2 + 1
        else
          dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
        end
      end
      dp[i][j] = (dp[i][j] + mod) % mod
    end
  end

  dp[0][n - 1]
end
