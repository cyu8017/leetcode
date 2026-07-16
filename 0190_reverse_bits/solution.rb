# LeetCode 0190 - Reverse Bits
# https://leetcode.com/problems/reverse-bits/

# @param {Integer} n
# @return {Integer}
def reverse_bits(n)
  result = 0
  32.times do
    result = (result << 1) | (n & 1)
    n >>= 1
  end
  result
end