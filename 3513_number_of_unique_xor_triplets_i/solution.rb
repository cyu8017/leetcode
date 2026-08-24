# LeetCode 3513 - Number of Unique XOR Triplets I
# https://leetcode.com/problems/number-of-unique-xor-triplets-i/

# @param {Integer[]} nums
# @return {Integer}
def unique_xor_triplets(nums)
  n = nums.length
  return n if n <= 2
  x = n
  length = 0
  while x != 0
    length += 1
    x >>= 1
  end
  1 << length
end
