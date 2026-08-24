# LeetCode 4002 - Count Valid Sequences
# https://leetcode.com/problems/count-valid-sequences/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def count_valid_sequences(n, k)
  mx = 500001
  mod = 1_000_000_007
  unless defined?($count_valid_sequences_f)
    $count_valid_sequences_f = Array.new(mx, 0)
    $count_valid_sequences_g = Array.new(mx, 0)
    $count_valid_sequences_f[0] = 1
    $count_valid_sequences_g[0] = 1
    mod_pow = lambda do |a, b|
      res = 1
      a %= mod
      while b > 0
        res = res * a % mod if (b & 1) != 0
        a = a * a % mod
        b >>= 1
      end
      res
    end
    (1...mx).each do |i|
      $count_valid_sequences_f[i] = $count_valid_sequences_f[i - 1] * i % mod
      $count_valid_sequences_g[i] = mod_pow.call($count_valid_sequences_f[i], mod - 2)
    end
  end
  comb = lambda do |nn, kk|
    return 0 if kk < 0 || kk > nn
    $count_valid_sequences_f[nn] * $count_valid_sequences_g[kk] % mod * $count_valid_sequences_g[nn - kk] % mod
  end
  ans = comb.call(n - 1, k - 1)
  ans = (ans - comb.call((n + k) / 2 - 1, k - 1) + mod) % mod if (n + k).even?
  ans
end
