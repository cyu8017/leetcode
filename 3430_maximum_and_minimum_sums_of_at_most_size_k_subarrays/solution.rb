# LeetCode 3430 - Maximum and Minimum Sums of at Most Size K Subarrays
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subarrays/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_max_subarray_sum(nums, k)
  n = nums.length
  ans = 0
  (0...n).each do |i|
    mn = mx = nums[i]
    j = i
    while j < n && j - i + 1 <= k
      mn = nums[j] if nums[j] < mn
      mx = nums[j] if nums[j] > mx
      ans += mn + mx
      j += 1
    end
  end
  ans
end
