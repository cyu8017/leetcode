# LeetCode 3535 - Unit Conversion II
# https://leetcode.com/problems/unit-conversion-ii/

# @param {Integer[][]} conversions
# @param {Integer[][]} queries
# @return {Integer[]}
def query_conversions(conversions, queries)
  mod = 1000000007
  qpow = lambda do |x, nn|
    res = 1
    bx = x
    bn = nn
    while bn > 0
      res = res * bx % mod if (bn & 1) != 0
      bx = bx * bx % mod
      bn >>= 1
    end
    res
  end
  n = conversions.length + 1
  g = Array.new(n) { [] }
  conversions.each { |e| g[e[0]] << [e[1], e[2]] }
  res = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |s, mul|
    res[s] = mul
    g[s].each { |to, w| dfs.call(to, mul * w % mod) }
  end
  dfs.call(0, 1)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    ans[i] = res[q[1]] * qpow.call(res[q[0]], mod - 2) % mod
  end
  ans
end
