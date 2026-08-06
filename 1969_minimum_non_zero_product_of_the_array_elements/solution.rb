# LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
# https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

# @param {Integer} p
# @return {Integer}
def min_non_zero_product(p)
  mod = 10**9 + 7
  mx = (1 << p) - 1
  mx * mod_pow(mx - 1, (1 << (p - 1)) - 1, mod) % mod
end

def mod_pow(base, exp, mod)
  result = 1
  base %= mod
  while exp.positive?
    result = result * base % mod if exp.odd?
    base = base * base % mod
    exp /= 2
  end
  result
end
