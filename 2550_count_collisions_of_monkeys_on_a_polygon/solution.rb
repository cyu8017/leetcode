# LeetCode 2550 - Count Collisions of Monkeys on a Polygon
# https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

# @param {Integer} n
# @return {Integer}
def monkey_move(n)
  mod = 1_000_000_007
  ((2.pow(n, mod) - 2) + mod) % mod
end
