# LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def max_palindromes(s, k)
  n = s.length
  is_pal = Array.new(n) { Array.new(n, false) }
  (0...n).each { |i| is_pal[i][i] = true }
  (0...(n - 1)).each { |i| is_pal[i][i + 1] = s[i] == s[i + 1] }
  (3..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length - 1
      is_pal[i][j] = s[i] == s[j] && is_pal[i + 1][j - 1]
    end
  end
  dp = Array.new(n + 1, 0)
  (n - 1).downto(0) do |i|
    dp[i] = dp[i + 1]
    (i + k - 1...n).each do |j|
      dp[i] = 1 + dp[j + 1] if is_pal[i][j] && 1 + dp[j + 1] > dp[i]
    end
  end
  dp[0]
end
