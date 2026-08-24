# LeetCode 0983 - Minimum Cost For Tickets
# https://leetcode.com/problems/minimum-cost-for-tickets/

# @param {Integer[]} days
# @param {Integer[]} costs
# @return {Integer}
def mincost_tickets(days, costs)
  dayset = days.to_h { |d| [d, true] }
  last = days[-1]
  dp = Array.new(last + 1, 0)
  (1..last).each do |d|
    if dayset[d]
      dp[d] = [
        dp[d - 1] + costs[0],
        dp[[0, d - 7].max] + costs[1],
        dp[[0, d - 30].max] + costs[2]
      ].min
    else
      dp[d] = dp[d - 1]
    end
  end
  dp[last]
end
