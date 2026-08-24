# LeetCode 2912 - Number of Ways to Reach Destination in the Grid
# https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @param {Integer[]} source
# @param {Integer[]} dest
# @return {Integer}
def number_of_ways(n, m, k, source, dest)
  mod = 1_000_000_007
  sx, sy = source[0], source[1]
  tx, ty = dest[0], dest[1]
  same = row = col = other = 0
  if sx == tx && sy == ty
    same = 1
  elsif sx == tx
    row = 1
  elsif sy == ty
    col = 1
  else
    other = 1
  end
  k.times do
    ns = (row + col) % mod
    nr = (same * (m - 1) + row * (m - 2) + other) % mod
    nc = (same * (n - 1) + col * (n - 2) + other) % mod
    no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4)) % mod
    same, row, col, other = ns, nr, nc, no
  end
  same
end
