# LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
# https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

# @param {Integer[]} price
# @param {Integer[]} tastiness
# @param {Integer} max_amount
# @param {Integer} max_coupons
# @return {Integer}
def max_tastiness(price, tastiness, max_amount, max_coupons)
  n = price.length
  neg = -(2_147_483_647 / 2)
  dp = Array.new(max_amount + 1) { Array.new(max_coupons + 1, neg) }
  dp[0][0] = 0
  (0...n).each do |i|
    p = price[i]
    t = tastiness[i]
    max_amount.downto(0) do |a|
      max_coupons.downto(0) do |c|
        next if dp[a][c] < 0

        dp[a + p][c] = [dp[a + p][c], dp[a][c] + t].max if a + p <= max_amount
        if c + 1 <= max_coupons && a + p / 2 <= max_amount
          half = a + p / 2
          dp[half][c + 1] = [dp[half][c + 1], dp[a][c] + t].max
        end
      end
    end
  end
  ans = 0
  (0..max_amount).each do |a|
    (0..max_coupons).each { |c| ans = dp[a][c] if dp[a][c] > ans }
  end
  ans
end
