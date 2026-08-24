# LeetCode 2935 - Maximum Strong Pair XOR II
# https://leetcode.com/problems/maximum-strong-pair-xor-ii/

# @param {Integer[]} nums
# @return {Integer}
def maximum_strong_pair_xor(nums)
  nums = nums.sort
  ans = 0
  nums.each_with_index do |x, i|
    j = i
    while j < nums.length && nums[j] <= 2 * x
      xorr = x ^ nums[j]
      ans = xorr if xorr > ans
      j += 1
    end
  end
  ans
end
