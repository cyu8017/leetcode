# LeetCode 2144 - Minimum Cost of Buying Candies With Discount
# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(cost)
  arr = cost.sort.reverse
  ans = 0
  arr.each_with_index { |x, i| ans += x if i % 3 != 2 }
  ans
end
