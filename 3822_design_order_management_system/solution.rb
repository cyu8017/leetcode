# LeetCode 3822 - Design Order Management System
# https://leetcode.com/problems/design-order-management-system/

class OrderManagementSystem
  def initialize
    @order_type_map = {}
    @price_map = {}
    @t = {}
  end

  def add_order(order_id, order_type, price)
    @order_type_map[order_id] = order_type
    @price_map[order_id] = price
    key = _key(order_type, price)
    @t[key] ||= []
    @t[key] << order_id
    nil
  end

  def modify_order(order_id, new_price)
    order_type = @order_type_map[order_id]
    old_price = @price_map[order_id]
    @price_map[order_id] = new_price
    old_key = _key(order_type, old_price)
    old_list = @t[old_key]
    old_list.each_with_index do |id, i|
      if id == order_id
        old_list.delete_at(i)
        break
      end
    end
    key = _key(order_type, new_price)
    @t[key] ||= []
    @t[key] << order_id
    nil
  end

  def cancel_order(order_id)
    order_type = @order_type_map.delete(order_id)
    price = @price_map.delete(order_id)
    key = _key(order_type, price)
    lst = @t[key]
    lst.each_with_index do |id, i|
      if id == order_id
        lst.delete_at(i)
        break
      end
    end
    nil
  end

  def get_orders_at_price(order_type, price)
    key = _key(order_type, price)
    lst = @t[key]
    return [] if lst.nil? || lst.empty?
    lst.reverse
  end

  def _key(order_type, price)
    "#{order_type}##{price}"
  end
end
