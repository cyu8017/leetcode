# LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
# https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_operations(nums1, nums2)
  calc = lambda do |a1, a2|
    n = a1.length
    ops = 0
    last1 = a1[n - 1]
    last2 = a2[n - 1]
    (0...n - 1).each do |i|
      x = a1[i]
      y = a2[i]
      next if x <= last1 && y <= last2
      if y <= last1 && x <= last2
        ops += 1
        next
      end
      return 1 << 30
    end
    ops
  end

  n = nums1.length
  ans = calc.call(nums1, nums2)
  t = nums1[n - 1]
  nums1[n - 1] = nums2[n - 1]
  nums2[n - 1] = t
  cand = calc.call(nums1, nums2) + 1
  ans = cand if cand < ans
  nums2[n - 1] = nums1[n - 1]
  nums1[n - 1] = t
  ans >= (1 << 30) ? -1 : ans
end
