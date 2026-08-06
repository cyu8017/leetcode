# LeetCode 1278 - Palindrome Partitioning III
# https://leetcode.com/problems/palindrome-partitioning-iii/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def palindrome_partition(s, k)
  n = s.length
  cost = Array.new(n) { Array.new(n, 0) }
  (2..n).each do |length|
    (0..n - length).each do |i|
      j = i + length - 1
      cost[i][j] = (length > 2 ? cost[i + 1][j - 1] : 0) + (s[i] == s[j] ? 0 : 1)
    end
  end
  inf = n + 1
  dp = Array.new(k + 1) { Array.new(n + 1, inf) }
  dp[0][0] = 0
  (1..k).each do |parts|
    (parts..n).each do |finish|
      dp[parts][finish] = ((parts - 1)...finish).map { |start| dp[parts - 1][start] + cost[start][finish - 1] }.min
    end
  end
  dp[k][n]
end
