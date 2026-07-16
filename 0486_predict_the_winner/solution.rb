# LeetCode 0486 - Predict the Winner
# https://leetcode.com/problems/predict-the-winner/

class Solution
  def predict_the_winner(nums)
    n = nums.length
    dp = Array.new(n) { Array.new(n, 0) }
    (0...n).each { |i| dp[i][i] = nums[i] }
    (2..n).each do |length|
      (0..(n - length)).each do |left|
        right = left + length - 1
        dp[left][right] = [
          nums[left] - dp[left + 1][right],
          nums[right] - dp[left][right - 1]
        ].max
      end
    end
    dp[0][n - 1] >= 0
  end

  alias_method :predictTheWinner, :predict_the_winner
end
