# LeetCode 2297 - Jump Game VIII
# https://leetcode.com/problems/jump-game-viii/

# @param {Integer[]} nums
# @param {Integer[]} costs
# @return {Integer}
def min_cost(nums, costs)
  n = nums.length
  dp = Array.new(n, Float::INFINITY)
  dp[0] = 0
  stack1 = []
  stack2 = []
  n.times do |i|
    while !stack1.empty? && nums[stack1[-1]] <= nums[i]
      j = stack1.pop
      dp[i] = [dp[i], dp[j] + costs[i]].min
    end
    while !stack2.empty? && nums[stack2[-1]] > nums[i]
      j = stack2.pop
      dp[i] = [dp[i], dp[j] + costs[i]].min
    end
    dp[i] = [dp[i], dp[stack1[-1]] + costs[i]].min unless stack1.empty?
    dp[i] = [dp[i], dp[stack2[-1]] + costs[i]].min unless stack2.empty?
    stack1 << i
    stack2 << i
  end
  dp[n - 1].to_i
end

alias solve min_cost
