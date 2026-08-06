# LeetCode 1475 - Final Prices With A Special Discount In A Shop
# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

def final_prices(prices)
  ans = prices.dup
  stack = []
  prices.each_with_index do |price, i|
    while !stack.empty? && prices[stack[-1]] >= price
      j = stack.pop
      ans[j] -= price
    end
    stack << i
  end
  ans
end
