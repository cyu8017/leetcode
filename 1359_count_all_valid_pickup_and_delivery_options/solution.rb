# LeetCode 1359 - Count All Valid Pickup And Delivery Options
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

def count_orders(n)
  ans = 1
  (1..n).each { |i| ans = ans * i * (2 * i - 1) % 1_000_000_007 }
  ans
end
