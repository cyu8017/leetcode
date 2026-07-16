# LeetCode 0188 - Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# @param {Integer} k
# @param {Integer[]} prices
# @return {Integer}
def max_profit(k, prices)
  return 0 if prices.empty? || k.zero?

  if k >= prices.length / 2
    return (1...prices.length).sum { |index| [prices[index] - prices[index - 1], 0].max }
  end

  buy = Array.new(k + 1, Float::INFINITY)
  sell = Array.new(k + 1, 0)
  prices.each do |price|
    (1..k).each do |transaction|
      buy[transaction] = [buy[transaction], price - sell[transaction - 1]].min
      sell[transaction] = [sell[transaction], price - buy[transaction]].max
    end
  end

  sell[k]
end