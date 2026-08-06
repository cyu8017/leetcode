// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

object Solution {
  def minCostToMoveChips(position: Array[Int]): Int = {
    val odd = position.count(x => (x & 1) == 1)
    math.min(odd, position.length - odd)
  }
}
