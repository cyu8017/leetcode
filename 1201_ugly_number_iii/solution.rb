# LeetCode 1201 - Ugly Number III
# https://leetcode.com/problems/ugly-number-iii/

# @param {Integer} n
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def nth_ugly_number(n, a, b, c)
  lcm = ->(x, y) { x / x.gcd(y) * y }
  ab = lcm.call(a, b)
  ac = lcm.call(a, c)
  bc = lcm.call(b, c)
  abc = lcm.call(ab, c)
  count = lambda do |x|
    x / a + x / b + x / c - x / ab - x / ac - x / bc + x / abc
  end
  lo = 1
  hi = 2_000_000_000
  while lo < hi
    mid = (lo + hi) / 2
    if count.call(mid) >= n
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
