# LeetCode 3418 - Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

# @param {Integer[][]} coins
# @return {Integer}
def maximum_amount(coins)
  m = coins.length
  n = coins[0].length
  neg = -(1 << 30)
  dp = Array.new(m) { Array.new(n) { Array.new(3, neg) } }
  if coins[0][0] < 0
    dp[0][0][0] = coins[0][0]
    dp[0][0][1] = 0
    dp[0][0][2] = 0
  else
    dp[0][0][0] = coins[0][0]
    dp[0][0][1] = coins[0][0]
    dp[0][0][2] = coins[0][0]
  end
  (0...m).each do |i|
    (0...n).each do |j|
      next if i == 0 && j == 0

      (0...3).each do |k|
        best = neg
        best = [best, dp[i - 1][j][k]].max if i > 0
        best = [best, dp[i][j - 1][k]].max if j > 0
        next if best == neg

        if coins[i][j] >= 0
          dp[i][j][k] = best + coins[i][j]
        else
          dp[i][j][k] = [dp[i][j][k], best + coins[i][j]].max
        end
      end
      (1...3).each do |k|
        best = neg
        best = [best, dp[i - 1][j][k - 1]].max if i > 0
        best = [best, dp[i][j - 1][k - 1]].max if j > 0
        dp[i][j][k] = [dp[i][j][k], best].max if best != neg && coins[i][j] < 0
      end
    end
  end
  [dp[m - 1][n - 1][0], dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]].max
end
