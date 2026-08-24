# LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

# @param {Integer[]} nums
# @param {Integer} x
# @param {Integer} k
# @return {Integer}
def min_operations(nums, x, k)
  n = nums.length
  min_ops = Array.new(n - x + 1, 0)
  (0..(n - x)).each do |i|
    w = nums[i, x].sort
    med = w[(x - 1) / 2]
    ops = 0
    w.each { |v| ops += (v - med).abs }
    min_ops[i] = ops
  end
  inf = 10**18
  dp = Array.new(n + 1) { Array.new(k + 1, inf) }
  dp[n][0] = 0
  (n - 1).downto(0) do |i|
    (0..k).each do |j|
      dp[i][j] = dp[i + 1][j]
      if j > 0 && i + x <= n && min_ops[i] + dp[i + x][j - 1] < dp[i][j]
        dp[i][j] = min_ops[i] + dp[i + x][j - 1]
      end
    end
  end
  dp[0][k]
end
