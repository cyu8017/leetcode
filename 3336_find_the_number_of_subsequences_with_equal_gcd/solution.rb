# LeetCode 3336 - Find the Number of Subsequences With Equal GCD
# https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def gcd_int(a, b)
  return b if a == 0

  while b != 0
    a, b = b, a % b
  end
  a
end

# @param {Integer[]} nums
# @return {Integer}
def subsequence_pair_count(nums)
  mod = 1_000_000_007
  max_v = nums.max
  dp = Array.new(max_v + 1) { Array.new(max_v + 1, 0) }
  dp[0][0] = 1
  nums.each do |x|
    ndp = Array.new(max_v + 1) { Array.new(max_v + 1, 0) }
    (0..max_v).each do |a|
      (0..max_v).each { |b| ndp[a][b] = dp[a][b] }
    end
    (0..max_v).each do |a|
      (0..max_v).each do |b|
        next if dp[a][b] == 0

        na = a == 0 ? x : gcd_int(a, x)
        nb = b == 0 ? x : gcd_int(b, x)
        ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
        ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
      end
    end
    dp = ndp
  end
  ans = 0
  (1..max_v).each { |g| ans = (ans + dp[g][g]) % mod }
  ans
end
