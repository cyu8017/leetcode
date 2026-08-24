# LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def maximum_jumps(nums, target)
  n = nums.length
  dp = Array.new(n, -1)
  dp[0] = 0
  (0...n).each do |i|
    next if dp[i] < 0
    ((i + 1)...n).each do |j|
      dp[j] = [dp[j], dp[i] + 1].max if (nums[j] - nums[i]).abs <= target
    end
  end
  dp[n - 1]
end
