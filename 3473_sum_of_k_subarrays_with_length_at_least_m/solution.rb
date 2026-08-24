# LeetCode 3473 - Sum of K Subarrays With Length at Least M
# https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer} m
# @return {Integer}
def max_sum(nums, k, m)
  n = nums.length
  pref = Array.new(n + 1, 0)
  (0...n).each { |i| pref[i + 1] = pref[i] + nums[i] }
  neg = -(10**18)
  dp = Array.new(k + 1) { Array.new(n + 1, neg) }
  (0..(n)).each { |i| dp[0][i] = 0 }
  (1..k).each do |t|
    best = neg
    ((t * m)..n).each do |i|
      j = i - m
      best = [best, dp[t - 1][j] - pref[j]].max
      dp[t][i] = best + pref[i]
    end
    (1..n).each { |i| dp[t][i] = [dp[t][i], dp[t][i - 1]].max }
  end
  dp[k][n]
end
