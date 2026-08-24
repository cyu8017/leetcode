# LeetCode 2240 - Number of Ways to Buy Pens and Pencils
# https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/

# @param {Integer} total
# @param {Integer} cost1
# @param {Integer} cost2
# @return {Integer}
def ways_to_buy_pens_pencils(total, cost1, cost2)
  ans = 0
  pens = 0
  while pens * cost1 <= total
    remain = total - pens * cost1
    ans += remain / cost2 + 1
    pens += 1
  end
  ans
end
