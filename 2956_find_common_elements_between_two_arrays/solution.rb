# LeetCode 2956 - Find Common Elements Between Two Arrays
# https://leetcode.com/problems/find-common-elements-between-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def find_intersection_values(nums1, nums2)
  s1 = nums1.to_h { |v| [v, true] }
  s2 = nums2.to_h { |v| [v, true] }
  a = nums1.count { |v| s2[v] }
  b = nums2.count { |v| s1[v] }
  [a, b]
end
