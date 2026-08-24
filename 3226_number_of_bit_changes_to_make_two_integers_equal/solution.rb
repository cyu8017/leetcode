# LeetCode 3226 - Number of Bit Changes to Make Two Integers Equal
# https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def min_changes(n, k)
  return -1 if (n & k) != k
  x = n ^ k
  c = 0
  while x > 0
    c += x & 1
    x >>= 1
  end
  c
end
