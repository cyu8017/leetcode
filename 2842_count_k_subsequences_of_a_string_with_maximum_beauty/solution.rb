# LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

# @param {String} s
# @param {Integer} k
# @return {Integer}
def count_k_subsequences_with_max_beauty(s, k)
  mod = 1_000_000_007
  freq = Array.new(26, 0)
  s.each_char { |ch| freq[ch.ord - 97] += 1 }
  vals = freq.select { |f| f > 0 }.sort.reverse
  return 0 if vals.length < k

  threshold = vals[k - 1]
  need = 0
  avail = 0
  prod = 1
  vals.each do |v|
    if v > threshold
      prod = (prod * v) % mod
      need += 1
    elsif v == threshold
      avail += 1
    end
  end
  remain = k - need

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

  comb = lambda do |n, r|
    return 0 if r < 0 || r > n

    num = 1
    den = 1
    r.times do |i|
      num = (num * (n - i)) % mod
      den = (den * (i + 1)) % mod
    end
    (num * mod_pow.call(den, mod - 2)) % mod
  end

  prod = (prod * comb.call(avail, remain)) % mod
  remain.times { prod = (prod * threshold) % mod }
  prod
end
