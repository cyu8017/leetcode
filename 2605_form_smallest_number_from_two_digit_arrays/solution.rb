# LeetCode 2605 - Form Smallest Number From Two Digit Arrays
# https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_number(nums1, nums2)
  s1 = {}
  s2 = {}
  nums1.each { |x| s1[x] = true }
  nums2.each { |x| s2[x] = true }
  common = 10
  s1.each_key { |x| common = x if s2[x] && x < common }
  return common if common < 10

  a = nums1.min
  b = nums2.min
  [a * 10 + b, b * 10 + a].min
end
