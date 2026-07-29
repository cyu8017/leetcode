# LeetCode 1005 - Maximize Sum Of Array After K Negations
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def largest_sum_after_k_negations(nums, k)
  nums = nums.sort
  nums.each_index do |i|
    break if k.zero? || nums[i] >= 0

    nums[i] = -nums[i]
    k -= 1
  end
  if k.odd?
    nums.sort!
    nums[0] = -nums[0]
  end
  nums.sum
end
