# LeetCode 3699 - Number of ZigZag Arrays I
# https://leetcode.com/problems/number-of-zigzag-arrays-i/

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
    pref_down = Array.new(m + 1, 0)
    (0...m).each { |j| pref_down[j + 1] = (pref_down[j] + down[j]) % mod }
    nup = (0...m).map { |j| pref_down[j] }
    suf_up = Array.new(m + 1, 0)
    (m - 1).downto(0) { |j| suf_up[j] = (suf_up[j + 1] + up[j]) % mod }
    ndown = (0...m).map { |j| suf_up[j + 1] }
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
