# LeetCode 1648 - Sell Diminishing-Valued Colored Balls
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/

# @param {Integer[]} inventory
# @param {Integer} orders
# @return {Integer}
def max_profit(inventory, orders)
  mod = 1_000_000_007
  inventory = inventory.sort.reverse + [0]
  ans = 0
  (0...(inventory.length - 1)).each do |i|
    width = i + 1
    high = inventory[i]
    low = inventory[i + 1]
    balls = width * (high - low)
    take = [orders, balls].min
    full, rem = take.divmod(width)
    bottom = high - full
    ans += width * (high + bottom + 1) * full / 2 + rem * bottom
    orders -= take
    break if orders.zero?
  end
  ans % mod
end
