# LeetCode 1043 - Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/

# @param {Integer[]} arr
# @param {Integer} k
# @return {Integer}
def max_sum_after_partitioning(arr, k)
  n = arr.length
  dp = Array.new(n + 1, 0)
  (1..n).each do |i|
    best = 0
    (1..[k, i].min).each do |size|
      best = [best, arr[i - size]].max
      dp[i] = [dp[i], dp[i - size] + best * size].max
    end
  end
  dp[n]
end
