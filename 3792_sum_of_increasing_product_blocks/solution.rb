# LeetCode 3792 - Sum of Increasing Product Blocks
# https://leetcode.com/problems/sum-of-increasing-product-blocks/

# @param {Integer} n
# @return {Integer}
def sum_of_blocks(n)
  mod = 1_000_000_007
  ans = 0
  k = 1
  (1..n).each do |i|
    x = 1
    (k...(k + i)).each { |j| x = x * j % mod }
    ans = (ans + x) % mod
    k += i
  end
  ans
end
