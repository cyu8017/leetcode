# LeetCode 1922 - Count Good Numbers
# https://leetcode.com/problems/count-good-numbers/

# @param {Integer} n
# @return {Integer}
def count_good_numbers(n)
  mod = 10**9 + 7
  mod_pow(5, (n + 1) / 2, mod) * mod_pow(4, n / 2, mod) % mod
end

def mod_pow(base, exp, mod)
  result = 1
  base %= mod
  while exp.positive?
    result = result * base % mod if exp.odd?
    base = base * base % mod
    exp /= 2
  end
  result
end
