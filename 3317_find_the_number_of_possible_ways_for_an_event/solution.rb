# LeetCode 3317 - Find the Number of Possible Ways for an Event
# https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

# @param {Integer} a
# @param {Integer} e
# @param {Integer} mod
# @return {Integer}
def mod_pow(a, e, mod)
  r = 1
  a %= mod
  while e > 0
    r = r * a % mod if (e & 1) != 0
    a = a * a % mod
    e >>= 1
  end
  r
end

# @param {Integer} n
# @param {Integer} x
# @param {Integer} y
# @return {Integer}
def number_of_ways(n, x, y)
  mod = 1_000_000_007
  dp = Array.new(n + 1) { Array.new(x + 1, 0) }
  dp[0][0] = 1
  (1..n).each do |i|
    (1..[x, i].min).each do |j|
      dp[i][j] = (dp[i - 1][j - 1] + j * dp[i - 1][j] % mod) % mod
    end
  end
  fact = Array.new(x + 1, 0)
  fact[0] = 1
  (1..x).each { |i| fact[i] = fact[i - 1] * i % mod }
  ans = 0
  ypow = 1
  (1..[x, n].min).each do |k|
    ypow = ypow * y % mod
    perm = fact[x] * mod_pow(fact[x - k], mod - 2, mod) % mod
    ans = (ans + dp[n][k] * perm % mod * ypow % mod) % mod
  end
  ans
end
