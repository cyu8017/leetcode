# LeetCode 2370 - Longest Ideal Subsequence
# https://leetcode.com/problems/longest-ideal-subsequence/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_ideal_string(s, k)
  dp = Array.new(26, 0)
  ans = 0
  s.each_char do |ch|
    c = ch.ord - 97
    best = 0
    (0...26).each { |p| best = dp[p] if (c - p).abs <= k && dp[p] > best }
    dp[c] = best + 1
    ans = dp[c] if dp[c] > ans
  end
  ans
end
