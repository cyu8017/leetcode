# LeetCode 0901 - Online Stock Span
# https://leetcode.com/problems/online-stock-span/

class StockSpanner
  def initialize
    @stack = []
  end

  def next(price)
    span = 1
    while !@stack.empty? && @stack[-1][0] <= price
      span += @stack.pop[1]
    end
    @stack << [price, span]
    span
  end
end
