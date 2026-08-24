# LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
# https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

# @param {Integer} start_pos
# @param {Integer} end_pos
# @param {Integer} k
# @return {Integer}
def number_of_ways(start_pos, end_pos, k)
  mod = 1_000_000_007
  mod_pow = lambda do |a, e|
    res = 1
    base = a % mod
    while e > 0
      res = res * base % mod if e & 1 != 0
      base = base * base % mod
      e >>= 1
    end
    res
  end
  comb = lambda do |n, r|
    return 0 if r < 0 || r > n
    num = 1
    den = 1
    r.times do |i|
      num = num * (n - i) % mod
      den = den * (i + 1) % mod
    end
    num * mod_pow.call(den, mod - 2) % mod
  end
  diff = (end_pos - start_pos).abs
  return 0 if diff > k || (k - diff) % 2 != 0
  r = (k + diff) / 2
  comb.call(k, r)
end
