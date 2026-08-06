# LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

# @param {Integer[]} arr
# @param {Integer} difference
# @return {Integer}
def longest_subsequence(arr, difference)
  dp = {}
  arr.each { |x| dp[x] = dp.fetch(x - difference, 0) + 1 }
  dp.values.max
end
