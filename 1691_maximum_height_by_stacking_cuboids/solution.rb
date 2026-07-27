# LeetCode 1691 - Maximum Height by Stacking Cuboids
# https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

# @param {Integer[][]} cuboids
# @return {Integer}
def max_height(cuboids)
  a = cuboids.map(&:sort).sort
  n = a.length
  dp = Array.new(n, 0)
  n.times do |i|
    dp[i] = a[i][2]
    i.times do |j|
      dp[i] = [dp[i], dp[j] + a[i][2]].max if (0...3).all? { |d| a[j][d] <= a[i][d] }
    end
  end
  dp.max
end
