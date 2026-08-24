# LeetCode 2220 - Minimum Bit Flips to Convert Number
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

# @param {Integer} start
# @param {Integer} goal
# @return {Integer}
def min_bit_flips(start, goal)
  x = start ^ goal
  ans = 0
  while x > 0
    ans += x & 1
    x >>= 1
  end
  ans
end
