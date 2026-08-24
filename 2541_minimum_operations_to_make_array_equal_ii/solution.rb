# LeetCode 2541 - Minimum Operations to Make Array Equal II
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} k
# @return {Integer}
def min_operations(nums1, nums2, k)
  if k == 0
    nums1.each_with_index { |x, i| return -1 if x != nums2[i] }
    return 0
  end
  pos = 0
  neg = 0
  nums1.each_with_index do |x, i|
    d = x - nums2[i]
    return -1 if d % k != 0

    if d > 0
      pos += d / k
    else
      neg += (-d) / k
    end
  end
  pos != neg ? -1 : pos
end
