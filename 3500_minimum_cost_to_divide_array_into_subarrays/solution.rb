# LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
# https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

# @param {Integer[]} nums
# @param {Integer[]} cost
# @param {Integer} k
# @return {Integer}
def minimum_cost(nums, cost, k)
  n = nums.length
  pn = Array.new(n + 1, 0)
  pc = Array.new(n + 1, 0)
  (0...n).each do |i|
    pn[i + 1] = pn[i] + nums[i]
    pc[i + 1] = pc[i] + cost[i]
  end
  inf = 10**18
  dp = Array.new(n + 1, 0)
  (0...n).each { |i| dp[i] = inf }
  (n - 1).downto(0) do |i|
    (i...n).each do |j|
      cand = pn[j + 1] * (pc[j + 1] - pc[i]) + k * (pc[n] - pc[i]) + dp[j + 1]
      dp[i] = cand if cand < dp[i]
    end
  end
  dp[0]
end
