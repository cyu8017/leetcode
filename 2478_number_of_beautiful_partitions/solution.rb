# LeetCode 2478 - Number of Beautiful Partitions
# https://leetcode.com/problems/number-of-beautiful-partitions/

# @param {String} s
# @param {Integer} k
# @param {Integer} min_length
# @return {Integer}
def beautiful_partitions(s, k, min_length)
  mod = 1_000_000_007
  is_prime = lambda { |c| c == "2" || c == "3" || c == "5" || c == "7" }
  n = s.length
  return 0 if !is_prime.call(s[0]) || is_prime.call(s[n - 1])

  dp = Array.new(k + 1) { Array.new(n + 1, 0) }
  dp[0][0] = 1
  (1..k).each do |p|
    pref = 0
    j = 0
    (1..n).each do |i|
      while j <= i - min_length
        pref = (pref + dp[p - 1][j]) % mod if j == 0 || (is_prime.call(s[j]) && !is_prime.call(s[j - 1]))
        j += 1
      end
      dp[p][i] = pref unless is_prime.call(s[i - 1])
    end
  end
  dp[k][n]
end
