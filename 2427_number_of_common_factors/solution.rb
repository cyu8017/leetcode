# LeetCode 2427 - Number of Common Factors
# https://leetcode.com/problems/number-of-common-factors/

# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def common_factors(a, b)
  gcd = lambda do |x, y|
    while y != 0
      x, y = y, x % y
    end
    x
  end

  g = gcd.call(a, b)
  ans = 0
  i = 1
  while i * i <= g
    if g % i == 0
      ans += 1
      ans += 1 if i * i != g
    end
    i += 1
  end
  ans
end
