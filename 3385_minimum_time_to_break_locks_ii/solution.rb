# LeetCode 3385 - Minimum Time to Break Locks II
# https://leetcode.com/problems/minimum-time-to-break-locks-ii/

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
# @return {Integer}
def find_minimum_time(strength)
  n = strength.length
  nn = 1 << n
  inf = 1e18
  dp = Array.new(nn, inf)
  dp[0] = 0
  k = 1
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
  dp[nn - 1].to_i
end
