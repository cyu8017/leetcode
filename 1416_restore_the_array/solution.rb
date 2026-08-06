# LeetCode 1416 - Restore The Array
# https://leetcode.com/problems/restore-the-array/

def number_of_arrays(s, k)
  mod = 1_000_000_007
  n = s.length
  dp = Array.new(n + 1, 0)
  dp[n] = 1
  (n - 1).downto(0) do |i|
    next if s[i] == '0'
    value = 0
    (i...n).each do |j|
      value = value * 10 + s[j].to_i
      break if value > k
      dp[i] = (dp[i] + dp[j + 1]) % mod
    end
  end
  dp[0]
end
