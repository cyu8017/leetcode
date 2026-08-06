# LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

# @param {Integer[]} customers
# @param {Integer} boarding_cost
# @param {Integer} running_cost
# @return {Integer}
def min_operations_max_profit(customers, boarding_cost, running_cost)
  waiting = profit = best = answer = rotation = 0
  i = 0
  while i < customers.length || waiting.positive?
    waiting += customers[i] if i < customers.length
    boarded = [4, waiting].min
    waiting -= boarded
    rotation += 1
    profit += boarded * boarding_cost - running_cost
    if profit > best
      best = profit
      answer = rotation
    end
    i += 1
  end
  best.positive? ? answer : -1
end
