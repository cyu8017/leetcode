# LeetCode 3700 - Number of ZigZag Arrays II
# https://leetcode.com/problems/number-of-zigzag-arrays-ii/

# @param {Integer} n
# @param {Integer} l
# @param {Integer} r
# @return {Integer}
def zig_zag_arrays(n, l, r)
  mod = 1_000_000_007
  m = r - l + 1
  return m % mod if n == 1

  up = Array.new(m, 1)
  down = Array.new(m, 1)
  (2..n).each do
    pref = Array.new(m + 1, 0)
    (0...m).each { |j| pref[j + 1] = (pref[j] + down[j]) % mod }
    nup = (0...m).map { |j| pref[j] }
    suf = Array.new(m + 1, 0)
    (m - 1).downto(0) { |j| suf[j] = (suf[j + 1] + up[j]) % mod }
    ndown = (0...m).map { |j| suf[j + 1] }
    up = nup
    down = ndown
  end
  ans = 0
  (0...m).each do |j|
    ans = (ans + up[j]) % mod
    ans = (ans + down[j]) % mod
  end
  ans
end
