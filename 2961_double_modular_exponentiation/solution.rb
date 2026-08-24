# LeetCode 2961 - Double Modular Exponentiation
# https://leetcode.com/problems/double-modular-exponentiation/

# @param {Integer[][]} variables
# @param {Integer} target
# @return {Integer[]}
def get_good_indices(variables, target)
  ans = []
  variables.each_with_index do |v, i|
    a, b, c, m = v
    ans << i if mod_pow(mod_pow(a, b, 10), c, m) == target
  end
  ans
end

def mod_pow(a, b, mod)
  res = 1 % mod
  a %= mod
  while b > 0
    res = res * a % mod if (b & 1) != 0
    a = a * a % mod
    b >>= 1
  end
  res
end
