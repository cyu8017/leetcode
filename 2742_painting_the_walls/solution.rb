# LeetCode 2742 - Painting the Walls
# https://leetcode.com/problems/painting-the-walls/

# @param {Integer[]} cost
# @param {Integer[]} time
# @return {Integer}
def paint_walls(cost, time)
  n = cost.length
  inf = 10**18
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  (0...n).each do |i|
    n.downto(0) do |j|
      nj = [n, j + time[i] + 1].min
      dp[nj] = dp[j] + cost[i] if dp[j] + cost[i] < dp[nj]
    end
  end
  dp[n]
end
