# LeetCode 3702 - Longest Subsequence With Non-Zero Bitwise XOR
# https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  xorv = 0
  cnt0 = 0
  nums.each do |x|
    xorv ^= x
    cnt0 += 1 if x == 0
  end
  n = nums.length
  return n if xorv != 0
  return 0 if cnt0 == n

  n - 1
end
