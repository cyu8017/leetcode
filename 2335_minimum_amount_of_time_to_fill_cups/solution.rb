# LeetCode 2335 - Minimum Amount of Time to Fill Cups
# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

# @param {Integer[]} amount
# @return {Integer}
def fill_cups(amount)
  a, b, c = amount[0], amount[1], amount[2]
  a, b = b, a if a < b
  a, c = c, a if a < c
  b, c = c, b if b < c
  return a if a >= b + c
  (a + b + c + 1) / 2
end
