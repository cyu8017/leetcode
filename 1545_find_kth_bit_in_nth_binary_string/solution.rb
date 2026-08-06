# LeetCode 1545 - Find Kth Bit in Nth Binary String
# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

# @param {Integer} n
# @param {Integer} k
# @return {Character}
def find_kth_bit(n, k)
  invert = false
  length = (1 << n) - 1
  while k != 1
    middle = length / 2 + 1
    if k == middle
      return invert ? '0' : '1'
    end
    if k > middle
      k = length - k + 1
      invert = !invert
    end
    length /= 2
  end
  invert ? '1' : '0'
end
