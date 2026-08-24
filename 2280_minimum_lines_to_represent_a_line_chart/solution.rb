# LeetCode 2280 - Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

# @param {Integer[][]} stock_prices
# @return {Integer}
def minimum_lines(stock_prices)
  return 0 if stock_prices.length <= 1

  stock_prices = stock_prices.sort_by { |p| p[0] }
  ans = 1
  (2...stock_prices.length).each do |i|
    x0, y0 = stock_prices[i - 2]
    x1, y1 = stock_prices[i - 1]
    x2, y2 = stock_prices[i]
    ans += 1 if (y1 - y0) * (x2 - x1) != (y2 - y1) * (x1 - x0)
  end
  ans
end
