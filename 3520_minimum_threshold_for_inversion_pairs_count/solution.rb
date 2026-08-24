# LeetCode 3520 - Minimum Threshold for Inversion Pairs Count
# https://leetcode.com/problems/minimum-threshold-for-inversion-pairs-count/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_threshold(nums, k)
  upper_bound = lambda do |a, target|
    lo = 0
    hi = a.length
    while lo < hi
      mid = (lo + hi) >> 1
      if a[mid] <= target
        lo = mid + 1
      else
        hi = mid
      end
    end
    lo
  end
  count_inv = lambda do |arr, kk, threshold|
    sorted_arr = []
    inv = 0
    arr.each do |num|
      left = upper_bound.call(sorted_arr, num)
      right = upper_bound.call(sorted_arr, num + threshold)
      inv += right - left
      sorted_arr.insert(upper_bound.call(sorted_arr, num), num)
    end
    inv >= kk
  end
  mx = 0
  nums.each { |v| mx = v if v > mx }
  l = 0
  r = mx + 1
  while l < r
    m = (l + r) >> 1
    if count_inv.call(nums, k, m)
      r = m
    else
      l = m + 1
    end
  end
  l > mx ? -1 : l
end
