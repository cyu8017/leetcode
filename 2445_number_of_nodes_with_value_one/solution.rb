# LeetCode 2445 - Number of Nodes With Value One
# https://leetcode.com/problems/number-of-nodes-with-value-one/

# @param {Integer} n
# @param {Integer[]} queries
# @return {Integer}
def number_of_nodes(n, queries)
  flip = Array.new(n + 1, 0)
  val = Array.new(n + 1, 0)
  queries.each { |q| flip[q] ^= 1 }
  ans = 0
  (1..n).each do |i|
    val[i] = flip[i]
    val[i] ^= val[i / 2] if i > 1
    ans += val[i]
  end
  ans
end
