# LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_space_wasted_k_resizing(nums, k)
  n = nums.length
  inf = 10**18
  waste = Array.new(n) { Array.new(n, 0) }
  n.times do |i|
    mx = total = 0
    (i...n).each do |j|
      mx = [mx, nums[j]].max
      total += nums[j]
      waste[i][j] = mx * (j - i + 1) - total
    end
  end
  segments = k + 1
  dp = Array.new(n + 1) { Array.new(segments + 1, inf) }
  dp[0][0] = 0
  (1..n).each do |i|
    (1..[segments, i].min).each do |s|
      (s - 1...i).each do |p|
        dp[i][s] = [dp[i][s], dp[p][s - 1] + waste[p][i - 1]].min
      end
    end
  end
  (1..segments).map { |s| dp[n][s] }.min
end
