# LeetCode 3463 - Check If Digits Are Equal in String After Operations II
# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-ii/

# @param {String} s
# @return {Boolean}
def has_same_digits(s)
  combine_digit_3463(s, 0) == combine_digit_3463(s, 1)
end

def mod_pow_p_3463(a, e, p)
  r = 1
  while e > 0
    r = r * a % p if e.odd?
    a = a * a % p
    e /= 2
  end
  r
end

def mod_inv_prime_3463(a, p)
  mod_pow_p_3463(a, p - 2, p)
end

def binom_mod_3463(n, k, p)
  return 0 if k < 0 || k > n

  num = 1
  den = 1
  (0...k).each do |i|
    num = num * (n - i) % p
    den = den * (i + 1) % p
  end
  num * mod_inv_prime_3463(den, p) % p
end

def crt_3463(a1, m1, a2, m2)
  (0...(m1 * m2)).each do |x|
    return x if x % m1 == a1 && x % m2 == a2
  end
  0
end

def binom_mod10_3463(n, k)
  crt_3463(binom_mod_3463(n, k, 2), 2, binom_mod_3463(n, k, 5), 5)
end

def combine_digit_3463(s, offset)
  n = s.length
  total = 0
  (0...(n - 1)).each do |i|
    total = (total + binom_mod10_3463(n - 2, i) * (s[i + offset].ord - 48)) % 10
  end
  total
end
