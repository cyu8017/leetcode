# LeetCode 3855 - Sum of K-Digit Numbers in a Range
# https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

# @param {Integer} l
# @param {Integer} r
# @param {Integer} k
# @return {Integer}
def sum_of_numbers(l, r, k)
  qpow = lambda do |a, n, mod|
    a %= mod
    res = 1
    while n > 0
      res = res * a % mod if n.odd?
      a = a * a % mod
      n >>= 1
    end
    res
  end
  mod = 1_000_000_007
  n = r - l + 1
  s = ((l + r) * n / 2) % mod
  part1 = qpow.call(n % mod, k - 1, mod)
  part2 = (qpow.call(10, k, mod) - 1 + mod) % mod
  inv9 = qpow.call(9, mod - 2, mod)
  ans = s
  ans = ans * part1 % mod
  ans = ans * part2 % mod
  ans * inv9 % mod
end
