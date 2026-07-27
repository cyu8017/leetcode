# LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

# @param {Integer} n
# @return {Integer}
def minimum_one_bit_operations(n)
  ans = 0
  while n.positive?
    ans ^= n
    n >>= 1
  end
  ans
end
