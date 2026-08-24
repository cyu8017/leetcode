# LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
# https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} score
# @return {Integer}
def max_profit(n, edges, score)
  popcount = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  need = Array.new(n, 0)
  dp = Array.new(1 << n, -1)
  dp[0] = 0
  edges.each { |e| need[e[1]] |= 1 << e[0] }
  (0...(1 << n)).each do |mask|
    next if dp[mask] < 0
    pos = popcount.call(mask) + 1
    (0...n).each do |i|
      next if ((mask >> i) & 1) != 0
      next unless (mask & need[i]) == need[i]
      nm = mask | (1 << i)
      v = dp[mask] + score[i] * pos
      dp[nm] = v if v > dp[nm]
    end
  end
  dp[(1 << n) - 1]
end
