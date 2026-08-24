# LeetCode 3131 - Find the Integer Added to Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def added_integer(nums1, nums2)
  nums2.min - nums1.min
end
