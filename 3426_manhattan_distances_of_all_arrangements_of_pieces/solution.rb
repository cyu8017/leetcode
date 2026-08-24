# LeetCode 3426 - Manhattan Distances of All Arrangements of Pieces
# https://leetcode.com/problems/manhattan-distances-of-all-arrangements-of-pieces/

# @param {Integer} m
# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def distance_sum(m, n, k)
  mod = 1_000_000_007
  return 0 if k < 2

  total_cells = m * n
  pair_choose = comb_3426(total_cells - 2, k - 2, mod)
  sum_dist = 0
  (1...m).each { |d| sum_dist += d * (m - d) * n * n }
  (1...n).each { |d| sum_dist += d * (n - d) * m * m }
  sum_dist % mod * pair_choose % mod
end

def mod_pow_3426(a, e, mod)
  r = 1
  base = a % mod
  while e > 0
    r = (r * base) % mod if (e & 1) != 0
    base = (base * base) % mod
    e >>= 1
  end
  r
end

def comb_3426(nn, kk, mod)
  return 0 if kk < 0 || kk > nn

  num = 1
  den = 1
  (0...kk).each do |i|
    num = num * (nn - i) % mod
    den = den * (i + 1) % mod
  end
  num * mod_pow_3426(den, mod - 2, mod) % mod
end
