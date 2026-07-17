# LeetCode 1716 - Calculate Money in Leetcode Bank
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

# @param {Integer} n
# @return {Integer}
def total_money(n)
  weeks, days = n.divmod(7)
  weeks * 28 + 7 * weeks * (weeks - 1) / 2 + days * (weeks + 1) + days * (days - 1) / 2
end
