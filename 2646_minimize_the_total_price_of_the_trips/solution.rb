# LeetCode 2646 - Minimize the Total Price of the Trips
# https://leetcode.com/problems/minimize-the-total-price-of-the-trips/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @param {Integer[][]} trips
# @return {Integer}
def minimum_total_price(n, edges, price, trips)
  g = Array.new(n) { [] }
  edges.each do |a, b|
    g[a] << b
    g[b] << a
  end
  cnt = Array.new(n, 0)
  path = nil
  path = lambda do |u, p, target|
    if u == target
      cnt[u] += 1
      return true
    end
    g[u].each do |v|
      next if v == p
      if path.call(v, u, target)
        cnt[u] += 1
        return true
      end
    end
    false
  end
  trips.each { |a, b| path.call(a, -1, b) }
  dfs = nil
  dfs = lambda do |u, p|
    full = price[u] * cnt[u]
    half = full / 2
    g[u].each do |v|
      next if v == p

      child = dfs.call(v, u)
      full += [child[0], child[1]].min
      half += child[0]
    end
    [full, half]
  end
  res = dfs.call(0, -1)
  [res[0], res[1]].min
end
