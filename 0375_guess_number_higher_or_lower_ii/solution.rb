# LeetCode 0375 - Guess Number Higher or Lower II
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/

class Solution
  def get_money_amount(n)
    dp = Array.new(n + 2) { Array.new(n + 2, 0) }

    2.upto(n) do |length|
      1.upto(n - length + 1) do |left|
        right = left + length - 1
        dp[left][right] = Float::INFINITY
        left.upto(right - 1) do |guess|
          cost = guess + [dp[left][guess - 1], dp[guess + 1][right]].max
          dp[left][right] = [dp[left][right], cost].min
        end
      end
    end

    dp[1][n]
  end

  alias_method :getMoneyAmount, :get_money_amount
end
