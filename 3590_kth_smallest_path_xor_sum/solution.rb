# LeetCode 3590 - Kth Smallest Path XOR Sum
# https://leetcode.com/problems/kth-smallest-path-xor-sum/

# @param {Integer[]} par
# @param {Integer[]} vals
# @param {Integer[][]} queries
# @return {Integer[]}
def kth_smallest(par, vals, queries)
  n = par.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[par[i]] << i }
  xor_path = Array.new(n, 0)
  dfs = nil
  dfs = lambda do |u|
    xor_path[u] ^= vals[u]
    g[u].each do |v|
      xor_path[v] = xor_path[u]
      dfs.call(v)
    end
  end
  dfs.call(0)
  in_t = Array.new(n, 0)
  out_t = Array.new(n, 0)
  order = []
  dfs2 = nil
  dfs2 = lambda do |u|
    in_t[u] = order.length
    order << xor_path[u]
    g[u].each { |v| dfs2.call(v) }
    out_t[u] = order.length
  end
  dfs2.call(0)
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    u, k = q[0], q[1]
    sub = order[in_t[u]...out_t[u]].sort
    uniq = []
    sub.each { |x| uniq << x if uniq.empty? || uniq[-1] != x }
    ans[i] = k > uniq.length ? -1 : uniq[k - 1]
  end
  ans
end
