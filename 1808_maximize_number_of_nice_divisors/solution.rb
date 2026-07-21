
MOD = 10**9 + 7

# @param {Integer} prime_factors
# @return {Integer}
def max_nice_divisors(prime_factors)
  return prime_factors if prime_factors <= 3
  if prime_factors % 3 == 0
    mod_pow(3, prime_factors / 3, MOD)
  elsif prime_factors % 3 == 1
    mod_pow(3, prime_factors / 3 - 1, MOD) * 4 % MOD
  else
    mod_pow(3, prime_factors / 3, MOD) * 2 % MOD
  end
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
