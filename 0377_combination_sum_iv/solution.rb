# LeetCode 0377 - Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/

class Solution
  def combination_sum4(nums, target)
    dp = Array.new(target + 1, 0)
    dp[0] = 1

    1.upto(target) do |amount|
      nums.each do |num|
        dp[amount] += dp[amount - num] if amount >= num
      end
    end

    dp[target]
  end

  alias_method :combinationSum4, :combination_sum4
end
