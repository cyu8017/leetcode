# LeetCode 2320 - Count Number of Ways to Place Houses
# https://leetcode.com/problems/count-number-of-ways-to-place-houses/

# @param {Integer} n
# @return {Integer}
def count_house_placements(n)
  mod = 1_000_000_007
  a = 1
  b = 1
  n.times { a, b = b, (a + b) % mod }
  ways = b % mod
  ways * ways % mod
end
