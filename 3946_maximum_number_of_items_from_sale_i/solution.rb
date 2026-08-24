# LeetCode 3946 - Maximum Number Of Items From Sale I
# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/

# @param {Integer[][]} items
# @param {Integer} budget
# @return {Integer}
def maximum_sale_items(items, budget)
  f = Array.new(budget + 1, 0)
  mn = 2_147_483_647
  items.each do |item|
    factor, price = item[0], item[1]
    mn = price if price < mn
    cnt = items.count { |j_item| j_item[0] % factor == 0 }
    budget.downto(price) do |j|
      v = f[j - price] + cnt
      f[j] = v if v > f[j]
    end
  end
  ans = 0
  (0..budget).each do |i|
    extra = (budget - i) / mn
    v = f[i] + extra
    ans = v if v > ans
  end
  ans
end
