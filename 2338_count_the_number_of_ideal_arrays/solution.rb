# LeetCode 2338 - Count the Number of Ideal Arrays
# https://leetcode.com/problems/count-the-number-of-ideal-arrays/

# @param {Integer} n
# @param {Integer} max_value
# @return {Integer}
def ideal_arrays(n, max_value)
  mod = 1_000_000_007
  max_len = 14
  comb = Array.new(n + 1) { Array.new(max_len + 1, 0) }
  (0..n).each do |i|
    comb[i][0] = 1
    (1..[max_len, i].min).each do |j|
      comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % mod
    end
  end
  dp = Array.new(max_value + 1) { Array.new(max_len + 1, 0) }
  (1..max_value).each { |i| dp[i][1] = 1 }
  (2..max_len).each do |length|
    (1..max_value).each do |v|
      m = 2 * v
      while m <= max_value
        dp[m][length] = (dp[m][length] + dp[v][length - 1]) % mod
        m += v
      end
    end
  end
  ans = 0
  (1..max_value).each do |v|
    (1..[max_len, n].min).each do |length|
      ans = (ans + (dp[v][length] * comb[n - 1][length - 1]) % mod) % mod
    end
  end
  ans
end
