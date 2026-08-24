# LeetCode 2481 - Minimum Cuts to Divide a Circle
# https://leetcode.com/problems/minimum-cuts-to-divide-a-circle/

# @param {Integer} n
# @return {Integer}
def number_of_cuts(n)
  return 0 if n == 1
  return n / 2 if n.even?

  n
end
