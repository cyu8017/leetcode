# LeetCode 3376 - Minimum Time to Break Locks I
# https://leetcode.com/problems/minimum-time-to-break-locks-i/

# @param {Integer} x
# @return {Integer}
def bits_ones(x)
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end

# @param {Integer[]} strength
# @param {Integer} k
# @return {Integer}
def find_minimum_time(strength, k)
  n = strength.length
  inf = 1_000_000_000
  nn = 1 << n
  dp = Array.new(nn, inf)
  dp[0] = 0
  nn.times do |mask|
    next if dp[mask] == inf

    opened = bits_ones(mask)
    x = 1 + opened * k
    n.times do |i|
      next if (mask & (1 << i)) != 0

      t = (strength[i] + x - 1) / x
      nmask = mask | (1 << i)
      dp[nmask] = dp[mask] + t if dp[mask] + t < dp[nmask]
    end
  end
  dp[nn - 1]
end
