# LeetCode 2110 - Number of Smooth Descent Periods of a Stock
# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

# @param {Integer[]} prices
# @return {Integer}
def get_descent_periods(prices)
  ans = cur = 1
  (1...prices.length).each do |i|
    cur = prices[i] == prices[i - 1] - 1 ? cur + 1 : 1
    ans += cur
  end
  ans
end
