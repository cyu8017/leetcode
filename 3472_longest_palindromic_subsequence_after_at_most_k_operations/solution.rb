# LeetCode 3472 - Longest Palindromic Subsequence After at Most K Operations
# https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def longest_palindromic_subsequence(s, k)
  n = s.length
  dp = Array.new(n) { Array.new(n) { Array.new(k + 1, -1) } }
  dist_circ = lambda do |a, b|
    d = (a.ord - b.ord).abs
    [d, 26 - d].min
  end
  dfs = nil
  dfs = lambda do |i, j, ops|
    return 0 if i > j
    return 1 if i == j
    return dp[i][j][ops] if dp[i][j][ops] != -1

    best = dfs.call(i + 1, j, ops)
    best = [best, dfs.call(i, j - 1, ops)].max
    cost = dist_circ.call(s[i], s[j])
    best = [best, 2 + dfs.call(i + 1, j - 1, ops - cost)].max if cost <= ops
    dp[i][j][ops] = best
    best
  end
  dfs.call(0, n - 1, k)
end
