# LeetCode 2403 - Minimum Time to Kill All Monsters
# https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

# @param {Integer[]} power
# @return {Integer}
def minimum_time(power)
  bit_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  n = power.length
  nmask = 1 << n
  dp = Array.new(nmask, 10**18)
  dp[0] = 0
  (0...nmask).each do |mask|
    killed = bit_count.call(mask)
    gain = killed + 1
    (0...n).each do |i|
      next if (mask & (1 << i)) != 0
      need = (power[i] + gain - 1) / gain
      nm = mask | (1 << i)
      cand = dp[mask] + need
      dp[nm] = cand if cand < dp[nm]
    end
  end
  dp[nmask - 1]
end

alias solve minimum_time
