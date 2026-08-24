# LeetCode 2872 - Maximum Number of K-Divisible Components
# https://leetcode.com/problems/maximum-number-of-k-divisible-components/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} values
# @param {Integer} k
# @return {Integer}
def max_k_divisible_components(n, edges, values, k)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  ans = 0

  dfs = lambda do |u, p|
    s = values[u] % k
    g[u].each do |v|
      next if v == p

      s = (s + dfs.call(v, u)) % k
    end
    ans += 1 if s == 0
    s
  end

  dfs.call(0, -1)
  ans
end
