# LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
# https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

# @param {Integer[]} nums
# @return {Integer}
def longest_subsequence(nums)
  n = nums.length
  ans = 1
  dp = Array.new(n) { Array.new(301, 0) }
  (0...n).each do |i|
    (0...i).each do |j|
      d = (nums[i] - nums[j]).abs
      best = 1
      (d..300).each do |pd|
        best = dp[j][pd] if dp[j][pd] > best
      end
      dp[i][d] = best + 1 if best + 1 > dp[i][d]
      ans = dp[i][d] if dp[i][d] > ans
    end
    dp[i][0] = 1 if dp[i][0] < 1
  end
  ans
end
