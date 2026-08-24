# LeetCode 2809 - Minimum Time to Make Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @param {Integer} x
# @return {Integer}
def minimum_time(nums1, nums2, x)
  n = nums1.length
  arr = (0...n).map { |i| [nums1[i], nums2[i]] }
  sum1 = nums1.sum
  sum2 = nums2.sum
  arr.sort_by! { |p| p[1] }
  dp = Array.new(n + 1, 0)
  (0...n).each do |i|
    (i + 1).downto(1) do |j|
      dp[j] = [dp[j], dp[j - 1] + arr[i][0] + j * arr[i][1]].max
    end
  end
  (0..n).each { |t| return t if sum1 + sum2 * t - dp[t] <= x }
  -1
end
