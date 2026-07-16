# LeetCode 0312 - Burst Balloons
# https://leetcode.com/problems/burst-balloons/

class Solution
  def maxCoins(nums)
    balloons = [1] + nums + [1]
    size = balloons.length
    dp = Array.new(size) { Array.new(size, 0) }
    (3..size).each do |length|
      (0..(size - length)).each do |left|
        right = left + length - 1
        ((left + 1)...right).each do |mid|
          coins = dp[left][mid] + dp[mid][right] +
                  balloons[left] * balloons[mid] * balloons[right]
          dp[left][right] = [dp[left][right], coins].max
        end
      end
    end
    dp[0][size - 1]
  end
end
