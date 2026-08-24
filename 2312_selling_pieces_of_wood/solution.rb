# LeetCode 2312 - Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/

# @param {Integer} m
# @param {Integer} n
# @param {Integer[][]} prices
# @return {Integer}
def selling_wood(m, n, prices)
  price = Array.new(m + 1) { Array.new(n + 1, 0) }
  dp = Array.new(m + 1) { Array.new(n + 1, 0) }
  prices.each do |h, w, p|
    price[h][w] = p
  end
  (1..m).each do |h|
    (1..n).each do |w|
      best = price[h][w]
      (1...h).each { |i| best = [best, dp[i][w] + dp[h - i][w]].max }
      (1...w).each { |j| best = [best, dp[h][j] + dp[h][w - j]].max }
      dp[h][w] = best
    end
  end
  dp[m][n]
end
