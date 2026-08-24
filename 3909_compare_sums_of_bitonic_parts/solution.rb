# LeetCode 3909 - Compare Sums of Bitonic Parts
# https://leetcode.com/problems/compare-sums-of-bitonic-parts/

# @param {Integer[]} nums
# @return {Integer}
def compare_bitonic_sums(nums)
  l = nums[0]
  r = nums.sum
  (1...nums.length).each do |i|
    break if nums[i - 1] > nums[i]
    l += nums[i]
    r -= nums[i - 1]
  end
  return -1 if l == r
  l > r ? 0 : 1
end
