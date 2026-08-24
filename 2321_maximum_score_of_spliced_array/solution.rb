# LeetCode 2321 - Maximum Score Of Spliced Array
# https://leetcode.com/problems/maximum-score-of-spliced-array/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def maximums_spliced_array(nums1, nums2)
  kadane = lambda do |a, b|
    best = 0
    cur = 0
    s = 0
    a.each_index do |i|
      s += a[i]
      cur += b[i] - a[i]
      cur = 0 if cur < 0
      best = cur if cur > best
    end
    s + best
  end
  [kadane.call(nums1, nums2), kadane.call(nums2, nums1)].max
end
