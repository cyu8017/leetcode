# LeetCode 0693 - Binary Number with Alternating Bits
# https://leetcode.com/problems/binary-number-with-alternating-bits/

# @param {Integer} n
# @return {Boolean}
def has_alternating_bits(n)
  x = n ^ (n >> 1)
  (x & (x + 1)) == 0
end
