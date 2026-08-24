# LeetCode 3575 - Maximum Good Subtree Score
# https://leetcode.com/problems/maximum-good-subtree-score/

# @param {Integer[]} vals
# @param {Integer[]} par
# @return {Integer}
def good_subtree_sum(vals, par)
  mod = 1000000007
  n = vals.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[par[i]] << i }
  ans = [0]
  digit_mask = lambda do |x|
    v = x
    mask = 0
    return [1, 1, 0] if x == 0
    while x > 0
      d = x % 10
      return [0, 0, 0] if (mask & (1 << d)) != 0
      mask |= 1 << d
      x /= 10
    end
    [mask, 1, v]
  end
  dfs = nil
  dfs = lambda do |u|
    dp = { 0 => 0 }
    dm = digit_mask.call(vals[u])
    dp[dm[0]] = dm[2] if dm[1] == 1
    g[u].each do |c|
      child = dfs.call(c)
      ndp = {}
      dp.each do |k1, v1|
        child.each do |k2, v2|
          if (k1 & k2) == 0
            nm = k1 | k2
            ndp[nm] = [ndp[nm] || 0, v1 + v2].max
          end
        end
      end
      dp.each { |k, v| ndp[k] = [ndp[k] || 0, v].max }
      child.each { |k, v| ndp[k] = [ndp[k] || 0, v].max }
      dp = ndp
    end
    best = 0
    dp.each_value { |s| best = [best, s].max }
    ans[0] = (ans[0] + best) % mod
    dp
  end
  dfs.call(0)
  ans[0]
end
