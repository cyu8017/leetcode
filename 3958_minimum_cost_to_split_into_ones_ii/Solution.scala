// LeetCode 3958 - Minimum Cost to Split Into Ones II
// https://leetcode.com/problems/minimum-cost-to-split-into-ones-ii/

object Solution {
  def minCost(n: Int): Long = n.toLong * (n - 1) / 2
}
