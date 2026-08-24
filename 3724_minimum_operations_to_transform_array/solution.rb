# LeetCode 3724 - Minimum Operations to Transform Array
# https://leetcode.com/problems/minimum-operations-to-transform-array/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
  ans = 1
  n = nums1.length
  ok = false
  d = 1 << 30
  (0...n).each do |i|
    x = [nums1[i], nums2[i]].max
    y = [nums1[i], nums2[i]].min
    ans += x - y
    d = [d, [(x - nums2[n]).abs, (y - nums2[n]).abs].min].min
    ok = true if nums2[n] >= y && nums2[n] <= x
  end
  ans += d unless ok
  ans
end
