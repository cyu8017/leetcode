# LeetCode 0494 - Target Sum
# https://leetcode.com/problems/target-sum/

class Solution
  def find_target_sum_ways(nums, target)
    total = nums.sum
    return 0 if (total + target).odd? || target.abs > total

    need = (total + target) / 2
    dp = Array.new(need + 1, 0)
    dp[0] = 1
    nums.each do |num|
      need.downto(num) do |amount|
        dp[amount] += dp[amount - num]
      end
    end
    dp[need]
  end

  alias_method :findTargetSumWays, :find_target_sum_ways
end
