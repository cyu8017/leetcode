// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

object Solution {
  def numMovesStones(a: Int, b: Int, c: Int): Array[Int] = {
    val sorted = Array(a, b, c).sorted
    val x = sorted(0)
    val y = sorted(1)
    val z = sorted(2)
    val minMoves =
      if (z - x == 2) 0
      else if (y - x <= 2 || z - y <= 2) 1
      else 2
    Array(minMoves, z - x - 2)
  }
}
