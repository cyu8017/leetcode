# LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
# https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

# @param {Integer} n
# @param {Integer[][]} edges
# @param {Integer[]} price
# @return {Integer}
def max_output(n, edges, price)
  g = Array.new(n) { [] }
  edges.each do |e|
    g[e[0]] << e[1]
    g[e[1]] << e[0]
  end
  ans = 0

  dfs = lambda do |u, p|
    max_child = 0
    g[u].each do |v|
      next if v == p

      child = dfs.call(v, u)
      max_child = child if child > max_child
      ans = child if child > ans
    end
    price[u] + max_child
  end

  dfs.call(0, -1)
  ans
end
