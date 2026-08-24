# LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

# @param {Integer} n
# @return {Integer}
def string_count(n)
  return 0 if n < 4

  mod = 1_000_000_007
  mod_pow = lambda do |a, b|
    res = 1
    a %= mod
    while b > 0
      res = (res * a) % mod if (b & 1) != 0
      a = (a * a) % mod
      b >>= 1
    end
    res
  end

  (
    mod_pow.call(26, n) -
    (mod_pow.call(25, n - 1) * (75 + n)) +
    (mod_pow.call(24, n - 1) * (72 + 2 * n)) -
    (mod_pow.call(23, n - 1) * (23 + n))
  ) % mod
end
