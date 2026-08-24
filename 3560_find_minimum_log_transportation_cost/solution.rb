# LeetCode 3560 - Find Minimum Log Transportation Cost
# https://leetcode.com/problems/find-minimum-log-transportation-cost/

# @param {Integer} n
# @param {Integer} m
# @param {Integer} k
# @return {Integer}
def min_cutting_cost(n, m, k)
  x = [n, m].max
  return 0 if x <= k
  k * (x - k)
end
