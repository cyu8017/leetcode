# LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

# @param {Integer} n
# @param {Integer[]} present
# @param {Integer[]} future
# @param {Integer[][]} hierarchy
# @param {Integer} budget
# @return {Integer}
def max_profit(n, present, future, hierarchy, budget)
  g = Array.new(n + 1) { [] }
  hierarchy.each { |e| g[e[0]] << e[1] }
  dfs = nil
  dfs = lambda do |u|
    nxt = Array.new(budget + 1) { [0, 0] }
    g[u].each do |v|
      fv = dfs.call(v)
      budget.downto(0) do |j|
        (0..j).each do |jv|
          (0...2).each do |pre|
            nxt[j][pre] = [nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre]].max
          end
        end
      end
    end
    f = Array.new(budget + 1) { [0, 0] }
    price = future[u - 1]
    (0..budget).each do |j|
      (0...2).each do |pre|
        cost = present[u - 1] / (pre + 1)
        if j >= cost
          buy_profit = nxt[j - cost][1] + (price - cost)
          f[j][pre] = [nxt[j][0], buy_profit].max
        else
          f[j][pre] = nxt[j][0]
        end
      end
    end
    f
  end
  dfs.call(1)[budget][0]
end
