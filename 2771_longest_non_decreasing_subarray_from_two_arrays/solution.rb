# LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
# https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def max_non_decreasing_length(nums1, nums2)
  n = nums1.length
  dp1 = 1
  dp2 = 1
  ans = 1
  (1...n).each do |i|
    nd1 = 1
    nd2 = 1
    nd1 = [nd1, dp1 + 1].max if nums1[i] >= nums1[i - 1]
    nd1 = [nd1, dp2 + 1].max if nums1[i] >= nums2[i - 1]
    nd2 = [nd2, dp1 + 1].max if nums2[i] >= nums1[i - 1]
    nd2 = [nd2, dp2 + 1].max if nums2[i] >= nums2[i - 1]
    dp1 = nd1
    dp2 = nd2
    ans = [ans, dp1, dp2].max
  end
  ans
end
