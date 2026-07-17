# LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
  return -1 if nums1.length * 6 < nums2.length || nums2.length * 6 < nums1.length

  s1 = nums1.sum
  s2 = nums2.sum
  return 0 if s1 == s2

  if s1 < s2
    nums1, nums2 = nums2, nums1
    s1, s2 = s2, s1
  end
  diff = s1 - s2
  gains = (nums1.map { |x| x - 1 } + nums2.map { |x| 6 - x }).sort.reverse
  ops = 0
  gains.each do |gain|
    break if diff <= 0

    diff -= gain
    ops += 1
  end
  diff <= 0 ? ops : -1
end
