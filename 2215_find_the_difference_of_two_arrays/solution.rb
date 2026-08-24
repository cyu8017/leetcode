# LeetCode 2215 - Find the Difference of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[][]}
def find_difference(nums1, nums2)
  s1 = nums1.to_h { |x| [x, true] }
  s2 = nums2.to_h { |x| [x, true] }
  a = s1.keys.select { |x| !s2.key?(x) }
  b = s2.keys.select { |x| !s1.key?(x) }
  [a, b]
end
