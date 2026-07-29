# LeetCode 1060 - Missing Element in Sorted Array
# https://leetcode.com/problems/missing-element-in-sorted-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def missing_element(nums, k)
  missing = ->(i) { nums[i] - nums[0] - i }
  n = nums.length
  return nums[-1] + k - missing.call(n - 1) if k > missing.call(n - 1)

  lo = 0
  hi = n - 1
  while lo < hi
    mid = (lo + hi) / 2
    if missing.call(mid) < k
      lo = mid + 1
    else
      hi = mid
    end
  end
  nums[lo - 1] + k - missing.call(lo - 1)
end
