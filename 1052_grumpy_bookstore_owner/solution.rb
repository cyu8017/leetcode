# LeetCode 1052 - Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/

# @param {Integer[]} customers
# @param {Integer[]} grumpy
# @param {Integer} minutes
# @return {Integer}
def max_satisfied(customers, grumpy, minutes)
  base = customers.each_with_index.sum { |c, i| grumpy[i].zero? ? c : 0 }
  gain = best = 0
  customers.each_with_index do |c, i|
    gain += c if grumpy[i] == 1
    if i >= minutes && grumpy[i - minutes] == 1
      gain -= customers[i - minutes]
    end
    best = [best, gain].max
  end
  base + best
end
