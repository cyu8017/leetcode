# LeetCode 3349 - Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

# @param {Integer[]} nums
# @param {Integer} start
# @param {Integer} k
# @return {Boolean}
def increasing_run?(nums, start, k)
  (start...(start + k - 1)).each do |i|
    return false if nums[i] >= nums[i + 1]
  end
  true
end

# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def has_increasing_subarrays(nums, k)
  n = nums.length
  (0..(n - 2 * k)).each do |i|
    return true if increasing_run?(nums, i, k) && increasing_run?(nums, i + k, k)
  end
  false
end
