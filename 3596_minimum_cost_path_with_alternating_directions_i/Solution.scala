// LeetCode 3596 - Minimum Cost Path with Alternating Directions I
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-i/

object Solution {
  def minCost(m: Int, n: Int): Int = {
    if (m == 1 && n == 1) 1
    else if (m == 1 && n == 2) 3
    else if (m == 2 && n == 1) 3
    else -1
  }
}
