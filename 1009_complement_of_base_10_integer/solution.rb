# LeetCode 1009 - Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/

# @param {Integer} n
# @return {Integer}
def bitwise_complement(n)
  return 1 if n.zero?

  mask = (1 << n.bit_length) - 1
  n ^ mask
end
