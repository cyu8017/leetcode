# LeetCode 2774 - Array Upper Bound
# https://leetcode.com/problems/array-upper-bound/

# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def upper_bound(arr, target)
  lo = 0
  hi = arr.length
  while lo < hi
    mid = (lo + hi) >> 1
    if arr[mid] <= target
      lo = mid + 1
    else
      hi = mid
    end
  end
  return -1 if lo == 0 || arr[lo - 1] != target
  lo - 1
end
