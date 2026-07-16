# LeetCode 0372 - Super Pow
# https://leetcode.com/problems/super-pow/

class Solution
  def super_pow(a, b)
    mod = 1337
    a %= mod
    result = 1

    b.each do |digit|
      result = pow_mod(result, 10, mod) * pow_mod(a, digit, mod) % mod
    end

    result
  end

  alias_method :superPow, :super_pow

  private

  def pow_mod(base, exponent, mod)
    result = 1
    while exponent > 0
      result = result * base % mod if exponent.odd?
      base = base * base % mod
      exponent >>= 1
    end
    result
  end
end
