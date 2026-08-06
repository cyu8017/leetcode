# LeetCode 1418 - Display Table Of Food Orders In A Restaurant
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

def display_table(orders)
  foods = orders.map { |_, _, food| food }.uniq.sort
  tables = orders.map { |_, table, _| table.to_i }.uniq.sort
  counts = Hash.new(0)
  orders.each { |_, table, food| counts[[table.to_i, food]] += 1 }
  [['Table'] + foods] + tables.map { |table| [table.to_s] + foods.map { |food| counts[[table, food]].to_s } }
end
