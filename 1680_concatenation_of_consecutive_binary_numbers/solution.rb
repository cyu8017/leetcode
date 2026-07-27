# LeetCode 1680 - Concatenation of Consecutive Binary Numbers
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/

# @param {Integer} n
# @return {Integer}
def concatenated_binary(n)
  ans = 0
  bits = 0
  mod = 1_000_000_007
  (1..n).each do |x|
    bits += 1 if (x & (x - 1)).zero?
    ans = ((ans << bits) + x) % mod
  end
  ans
end
