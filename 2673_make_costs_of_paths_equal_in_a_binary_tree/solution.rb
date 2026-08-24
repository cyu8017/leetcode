# LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
# https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

# @param {Integer} n
# @param {Integer[]} cost
# @return {Integer}
def min_increments(n, cost)
  ans = 0
  (n / 2 - 1).downto(0) do |i|
    l = 2 * i + 1
    r = 2 * i + 2
    ans += (cost[l] - cost[r]).abs
    cost[i] += [cost[l], cost[r]].max
  end
  ans
end
