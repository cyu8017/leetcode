# LeetCode 2539 - Count the Number of Good Subsequences
# https://leetcode.com/problems/count-the-number-of-good-subsequences/

# @param {String} s
# @return {Integer}
def count_good_subsequences(s)
  mod = 1_000_000_007
  cnt = Array.new(26, 0)
  maxf = 0
  s.each_byte do |b|
    idx = b - 97
    cnt[idx] += 1
    maxf = cnt[idx] if cnt[idx] > maxf
  end

  mod_pow = lambda do |a, e|
    res = 1
    while e > 0
      res = res * a % mod if e.odd?
      a = a * a % mod
      e >>= 1
    end
    res
  end

  fact = Array.new(maxf + 1, 0)
  inv_fact = Array.new(maxf + 1, 0)
  fact[0] = 1
  (1..maxf).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact[maxf] = mod_pow.call(fact[maxf], mod - 2)
  maxf.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }

  comb = lambda do |n, k|
    return 0 if k < 0 || k > n

    fact[n] * inv_fact[k] % mod * inv_fact[n - k] % mod
  end

  ans = 0
  (1..maxf).each do |k|
    ways = 1
    26.times do |i|
      ways = ways * (1 + comb.call(cnt[i], k)) % mod if cnt[i] >= k
    end
    ans = (ans + ways - 1 + mod) % mod
  end
  ans
end

alias solve count_good_subsequences
