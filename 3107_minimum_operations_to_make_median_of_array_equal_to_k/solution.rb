# LeetCode 3107 - Minimum Operations to Make Median of Array Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-median-of-array-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations_to_make_median_k(nums, k)
  nums = nums.sort
  n = nums.length
  m = n >> 1
  ans = (nums[m] - k).abs
  if nums[m] > k
    i = m - 1
    while i >= 0 && nums[i] > k
      ans += nums[i] - k
      i -= 1
    end
  else
    i = m + 1
    while i < n && nums[i] < k
      ans += k - nums[i]
      i += 1
    end
  end
  ans
end
