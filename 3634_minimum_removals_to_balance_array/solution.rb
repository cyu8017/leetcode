# LeetCode 3634 - Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_removal(nums, k)
  nums = nums.sort
  n = nums.length
  lower_bound = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] < target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  cnt = 0
  (0...n).each do |i|
    j = n
    if nums[i] * k <= nums[n - 1]
      target = nums[i] * k + 1
      j = lower_bound.call(nums, target)
    end
    cnt = j - i if j - i > cnt
  end
  n - cnt
end
