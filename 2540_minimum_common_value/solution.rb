# LeetCode 2540 - Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def get_common(nums1, nums2)
  i = j = 0
  while i < nums1.length && j < nums2.length
    return nums1[i] if nums1[i] == nums2[j]

    if nums1[i] < nums2[j]
      i += 1
    else
      j += 1
    end
  end
  -1
end
