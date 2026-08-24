# LeetCode 0717 - 1-bit and 2-bit Characters
# https://leetcode.com/problems/1-bit-and-2-bit-characters/

# @param {Integer[]} bits
# @return {Boolean}
def is_one_bit_character(bits)
  i = 0
  n = bits.length
  while i < n - 1
    i += bits[i] == 1 ? 2 : 1
  end
  i == n - 1
end
