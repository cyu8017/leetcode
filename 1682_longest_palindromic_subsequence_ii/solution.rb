# LeetCode 1682 - Longest Palindromic Subsequence II
# https://leetcode.com/problems/longest-palindromic-subsequence-ii/

# @param {String} s
# @return {Integer}
def longest_palindrome_subseq(s)
  n = s.length
  dp = Array.new(n) { Array.new(n) { Array.new(26, 0) } }
  (2..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      26.times do |c|
        dp[i][j][c] = [dp[i + 1][j][c], dp[i][j - 1][c]].max
      end
      next unless s[i] == s[j]

      c = s[i].ord - 97
      inner = if length == 2
                0
              else
                (0...26).reject { |x| x == c }.map { |x| dp[i + 1][j - 1][x] }.max || 0
              end
      dp[i][j][c] = [dp[i][j][c], inner + 2].max
    end
  end
  dp[0][n - 1].max
end
