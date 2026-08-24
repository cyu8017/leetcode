# LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
# https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def min_subarray_sort(nums, k)
  f = lambda do |arr, i, j, inf|
    mi = inf
    mx = -inf
    l = -1
    r = -1
    (i..j).each do |p|
      if arr[p] < mx
        r = p
      else
        mx = arr[p]
      end
      q = j - p + i
      if arr[q] > mi
        l = q
      else
        mi = arr[q]
      end
    end
    return 0 if r == -1
    r - l + 1
  end
  inf = 1 << 30
  n = nums.length
  (0..(n - k)).map { |i| f.call(nums, i, i + k - 1, inf) }
end
