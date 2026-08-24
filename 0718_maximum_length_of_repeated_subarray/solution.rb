# LeetCode 0718 - Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def find_length(nums1, nums2)
  m = nums1.length
  n = nums2.length
  dp = Array.new(n + 1, 0)
  best = 0
  (1..m).each do |i|
    next_dp = Array.new(n + 1, 0)
    (1..n).each do |j|
      if nums1[i - 1] == nums2[j - 1]
        next_dp[j] = dp[j - 1] + 1
        best = [best, next_dp[j]].max
      end
    end
    dp = next_dp
  end
  best
end
