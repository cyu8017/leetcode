# LeetCode 3343 - Count Number of Balanced Permutations
# https://leetcode.com/problems/count-number-of-balanced-permutations/

# @param {Integer} a
# @param {Integer} e
# @param {Integer} mod
# @return {Integer}
def mod_pow(a, e, mod)
  r = 1
  a %= mod
  while e > 0
    r = r * a % mod if (e & 1) != 0
    a = a * a % mod
    e >>= 1
  end
  r
end

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def pack_key(a, b)
  (a << 32) | (b & 0xFFFFFFFF)
end

# @param {String} num
# @return {Integer}
def count_balanced_permutations(num)
  mod = 1_000_000_007
  cnt = Array.new(10, 0)
  ssum = 0
  num.each_char do |c|
    d = c.ord - 48
    cnt[d] += 1
    ssum += d
  end
  return 0 if ssum.odd?

  n = num.length
  half_n = n / 2
  half_s = ssum / 2
  fact = Array.new(n + 1, 0)
  inv_f = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_f[n] = mod_pow(fact[n], mod - 2, mod)
  n.downto(1) { |i| inv_f[i - 1] = inv_f[i] * i % mod }
  dp = { pack_key(0, 0) => 1 }
  10.times do |d|
    ndp = {}
    dp.each do |st, ways|
      used = st >> 32
      s = st & 0xFFFFFFFF
      (0..cnt[d]).each do |take|
        nu = used + take
        ns = s + take * d
        next if nu > half_n || ns > half_s

        w = ways * inv_f[take] % mod * inv_f[cnt[d] - take] % mod
        nk = pack_key(nu, ns)
        ndp[nk] = ((ndp[nk] || 0) + w) % mod
      end
    end
    dp = ndp
  end
  ans = dp[pack_key(half_n, half_s)] || 0
  ans = ans * fact[half_n] % mod * fact[n - half_n] % mod
  10.times { |d| ans = ans * fact[cnt[d]] % mod }
  ans
end
