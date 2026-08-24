# LeetCode 2247 - Maximum Cost of Trip With K Highways
# https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

# @param {Integer} n
# @param {Integer[][]} highways
# @param {Integer} k
# @return {Integer}
def maximum_cost(n, highways, k)
  return -1 if k + 1 > n

  g = Array.new(n) { [] }
  highways.each do |a, b, w|
    g[a] << [b, w]
    g[b] << [a, w]
  end
  dp = Array.new(1 << n) { Array.new(n, -1) }
  n.times { |i| dp[1 << i][i] = 0 }
  ans = -1
  (0...(1 << n)).each do |mask|
    cities = mask.to_s(2).count("1")
    n.times do |u|
      next if dp[mask][u] < 0

      ans = [ans, dp[mask][u]].max if cities - 1 == k
      g[u].each do |v, w|
        next if (mask & (1 << v)) != 0

        nm = mask | (1 << v)
        dp[nm][v] = [dp[nm][v], dp[mask][u] + w].max
      end
    end
  end
  ans
end

alias solve maximum_cost
