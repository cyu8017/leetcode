# LeetCode 0878 - Nth Magical Number
# https://leetcode.com/problems/nth-magical-number/

# @param {Integer} n
# @param {Integer} a
# @param {Integer} b
# @return {Integer}
def nth_magical_number(n, a, b)
  mod = 10**9 + 7
  lcm = a / a.gcd(b) * b
  lo = 1
  hi = n * [a, b].min
  while lo < hi
    mid = (lo + hi) / 2
    if mid / a + mid / b - mid / lcm >= n
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo % mod
end
