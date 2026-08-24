# LeetCode 3269 - Constructing Two Increasing Arrays
# https://leetcode.com/problems/constructing-two-increasing-arrays/

# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer}
def min_largest(nums1, nums2)
  n = nums1.length
  m = nums2.length
  inf = 1_000_000_000
  dp = Array.new(n + 1) { Array.new(m + 1, inf) }
  dp[0][0] = 0
  (0..n).each do |i|
    (0..m).each do |j|
      next if dp[i][j] == inf
      prev = dp[i][j]
      if i < n
        need = prev + 1
        if nums1[i] == 0
          need += 1 if need.odd?
        else
          need += 1 if need.even?
        end
        dp[i + 1][j] = need if need < dp[i + 1][j]
      end
      if j < m
        need = prev + 1
        if nums2[j] == 0
          need += 1 if need.odd?
        else
          need += 1 if need.even?
        end
        dp[i][j + 1] = need if need < dp[i][j + 1]
      end
    end
  end
  dp[n][m]
end
