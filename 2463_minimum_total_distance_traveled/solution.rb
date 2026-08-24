# LeetCode 2463 - Minimum Total Distance Traveled
# https://leetcode.com/problems/minimum-total-distance-traveled/

# @param {Integer[]} robot
# @param {Integer[][]} factory
# @return {Integer}
def minimum_total_distance(robot, factory)
  robots = robot.sort
  factory = factory.sort_by { |x| x[0] }
  m = robots.length
  pos = []
  factory.each { |f| f[1].times { pos << f[0] } }
  n = pos.length
  inf = 10**18
  dp = Array.new(m + 1) { Array.new(n + 1, inf) }
  (0..n).each { |j| dp[0][j] = 0 }
  (1..m).each do |i|
    (i..n).each do |j|
      dp[i][j] = dp[i][j - 1]
      diff = robots[i - 1] - pos[j - 1]
      diff = -diff if diff < 0
      dp[i][j] = dp[i - 1][j - 1] + diff if dp[i - 1][j - 1] + diff < dp[i][j]
    end
  end
  dp[m][n]
end
