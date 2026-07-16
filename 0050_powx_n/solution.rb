# LeetCode 0050 - Pow(x, n)
# https://leetcode.com/problems/powx-n/

# @param {Float} x
# @param {Integer} n
# @return {Float}
def my_pow(x, n)
  return 1.0 if n == 0

  base = x
  exponent = n
  if exponent < 0
    base = 1.0 / base
    exponent = -exponent
  end

  result = 1.0
  current = base

  while exponent != 0
    result *= current if exponent.odd?
    current *= current
    exponent >>= 1
  end

  result
end
