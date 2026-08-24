# LeetCode 3668 - Restore Finishing Order
# https://leetcode.com/problems/restore-finishing-order/

# @param {Integer[]} order
# @param {Integer[]} friends
# @return {Integer[]}
def recover_order(order, friends)
  n = order.length
  d = Array.new(n + 1, 0)
  order.each_with_index { |x, i| d[x] = i }
  friends.sort_by { |a| d[a] }
end
