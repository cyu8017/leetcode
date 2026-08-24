# LeetCode 0868 - Binary Gap
# https://leetcode.com/problems/binary-gap/

# @param {Integer} n
# @return {Integer}
def binary_gap(n)
  last = -1
  ans = 0
  bit = 0
  while n.positive?
    if n & 1 == 1
      ans = [ans, bit - last].max if last != -1
      last = bit
    end
    n >>= 1
    bit += 1
  end
  ans
end
