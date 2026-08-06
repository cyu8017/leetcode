# LeetCode 1357 - Apply Discount Every N Orders
# https://leetcode.com/problems/apply-discount-every-n-orders/

class Cashier
  def initialize(n, discount, products, prices)
    @n = n
    @discount = discount
    @price = {}
    products.each_with_index { |p, i| @price[p] = prices[i] }
    @count = 0
  end

  def get_bill(product, amount)
    @count += 1
    total = 0.0
    product.each_with_index { |p, i| total += @price[p] * amount[i] }
    @count % @n == 0 ? total * (100 - @discount) / 100.0 : total
  end
end
