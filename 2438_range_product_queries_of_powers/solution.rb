# LeetCode 2438 - Range Product Queries of Powers
# https://leetcode.com/problems/range-product-queries-of-powers/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def product_queries(n, queries)
  mod = 1_000_000_007
  powers = []
  (0...31).each { |bit| powers << (1 << bit) if ((n >> bit) & 1) != 0 }
  ans = Array.new(queries.length, 0)
  queries.each_with_index do |q, i|
    prod = 1
    q[0].upto(q[1]) { |j| prod = (prod * powers[j]) % mod }
    ans[i] = prod
  end
  ans
end
