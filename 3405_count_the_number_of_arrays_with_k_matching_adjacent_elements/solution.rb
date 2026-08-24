# LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
# https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def count_good_arrays(n, m, k)
  mod = 1_000_000_007
  (comb_3405(n - 1, k, mod) * m % mod * mod_pow_3405(m - 1, n - 1 - k, mod)) % mod
end

def mod_pow_3405(a, e, mod)
  r = 1
  base = ((a % mod) + mod) % mod
  exp = e
  while exp > 0
    r = (r * base) % mod if (exp & 1) != 0
    base = (base * base) % mod
    exp >>= 1
  end
  r
end

def comb_3405(nn, kk, mod)
  return 0 if kk < 0 || kk > nn

  num = 1
  den = 1
  (0...kk).each do |i|
    num = (num * (nn - i)) % mod
    den = (den * (i + 1)) % mod
  end
  (num * mod_pow_3405(den, mod - 2, mod)) % mod
end
