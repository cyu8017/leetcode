# LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
# https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

# @param {String} s
# @return {Integer}
def minimum_beautiful_substrings(s)
  n = s.length
  pow5 = {}
  x = 1
  loop do
    b = x.to_s(2)
    break if b.length > n
    pow5[b] = true
    x *= 5
  end
  inf = 10**9
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] == inf || s[i] == "0"
    ((i + 1)..n).each do |j|
      dp[j] = [dp[j], dp[i] + 1].min if pow5[s[i...j]]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
