
MOD = 10**9 + 7

# @param {String} s
# @return {Integer}
def make_string_sorted(s)
  n = s.length
  fact = Array.new(n + 1, 1)
  (2..n).each { |i| fact[i] = fact[i - 1] * i % MOD }

  inv_fact = Array.new(n + 1, 1)
  inv_fact[n] = mod_pow(fact[n], MOD - 2, MOD)
  (n - 1).downto(0) { |i| inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD }

  freq = Array.new(26, 0)
  s.each_char { |ch| freq[ch.ord - 'a'.ord] += 1 }

  ans = 0
  s.each_char.with_index do |ch, i|
    c = ch.ord - 'a'.ord
    (0...c).each do |smaller|
      next if freq[smaller] == 0
      freq[smaller] -= 1
      ways = fact[n - i - 1]
      freq.each { |count| ways = ways * inv_fact[count] % MOD }
      ans = (ans + ways) % MOD
      freq[smaller] += 1
    end
    freq[c] -= 1
  end
  ans
end

def mod_pow(base, exp, mod)
  result = 1
  b = base % mod
  e = exp
  while e > 0
    result = result * b % mod if e.odd?
    b = b * b % mod
    e /= 2
  end
  result
end
