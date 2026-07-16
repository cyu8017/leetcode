# LeetCode 0088 - Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

# @param {Integer[]} nums1
# @param {Integer} m
# @param {Integer[]} nums2
# @param {Integer} n
# @return {Void} Do not return anything, modify nums1 in-place instead.
def merge(nums1, m, nums2, n)
  i = m - 1
  j = n - 1
  write = m + n - 1

  while j >= 0
    if i >= 0 && nums1[i] > nums2[j]
      nums1[write] = nums1[i]
      i -= 1
    else
      nums1[write] = nums2[j]
      j -= 1
    end
    write -= 1
  end
end
