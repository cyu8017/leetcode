# LeetCode 3528 - Unit Conversion I
# https://leetcode.com/problems/unit-conversion-i/

# @param {Integer[][]} conversions
# @return {Integer[]}
def base_unit_conversions(conversions)
  mod = 1000000007
  n = conversions.length + 1
  g = Array.new(n) { [] }
  conversions.each { |e| g[e[0]] << [e[1], e[2]] }
  ans = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |s, mul|
    ans[s] = mul
    g[s].each { |to, w| dfs.call(to, mul * w % mod) }
  end
  dfs.call(0, 1)
  ans
end
