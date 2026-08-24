# LeetCode 2585 - Number of Ways to Earn Points
# https://leetcode.com/problems/number-of-ways-to-earn-points/

# @param {Integer} target
# @param {Integer[][]} types
# @return {Integer}
def ways_to_reach_target(target, types)
  mod = 1_000_000_007
  dp = Array.new(target + 1, 0)
  dp[0] = 1
  types.each do |count, marks|
    target.downto(0) do |s|
      k = 1
      while k <= count && s - k * marks >= 0
        dp[s] = (dp[s] + dp[s - k * marks]) % mod
        k += 1
      end
    end
  end
  dp[target]
end
