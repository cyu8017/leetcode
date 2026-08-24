# LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
# https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

# @param {Integer[][]} edges
# @param {Integer[]} coins
# @param {Integer} k
# @return {Integer}
def maximum_points(edges, coins, k)
  n = coins.length
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  memo = {}

  dfs = nil
  dfs = lambda do |u, p, shifts|
    shifts = 14 if shifts > 14
    key = (u << 5) | shifts
    return memo[key] if memo.key?(key)

    c = coins[u] >> shifts
    opt1 = c - k
    opt2 = c / 2
    g[u].each do |v|
      next if v == p

      opt1 += dfs.call(v, u, shifts)
      opt2 += dfs.call(v, u, shifts + 1)
    end
    best = [opt1, opt2].max
    memo[key] = best
    best
  end

  dfs.call(0, -1, 0)
end
