# LeetCode 2318 - Number of Distinct Roll Sequences
# https://leetcode.com/problems/number-of-distinct-roll-sequences/

# @param {Integer} n
# @return {Integer}
def distinct_sequences(n)
  mod = 1_000_000_007
  gcd = lambda do |a, b|
    a, b = b, a % b while b != 0
    a
  end
  dp = Array.new(n + 1) { Array.new(7) { Array.new(7, 0) } }
  (1..6).each { |a| dp[1][a][0] = 1 }
  (2..n).each do |i|
    (1..6).each do |prev|
      (0..6).each do |pprev|
        next if dp[i - 1][prev][pprev] == 0
        (1..6).each do |cur|
          next if cur == prev || cur == pprev || gcd.call(cur, prev) != 1
          dp[i][cur][prev] = (dp[i][cur][prev] + dp[i - 1][prev][pprev]) % mod
        end
      end
    end
  end
  ans = 0
  (1..6).each do |a|
    (0..6).each { |b| ans = (ans + dp[n][a][b]) % mod }
  end
  ans
end
