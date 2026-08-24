# LeetCode 3857 - Minimum Cost to Split into Ones
# https://leetcode.com/problems/minimum-cost-to-split-into-ones/

# @param {Integer} n
# @return {Integer}
def min_cost(n)
  n * (n - 1) / 2
end
