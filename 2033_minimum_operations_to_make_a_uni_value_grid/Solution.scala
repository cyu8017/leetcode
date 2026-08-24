// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

object Solution {
  def minOperations(grid: Array[Array[Int]], x: Int): Int = {
    val vals = scala.collection.mutable.ArrayBuffer.empty[Int]
    val bas = grid(0)(0) % x
    grid.foreach { row =>
      row.foreach { v =>
        if (v % x != bas) return -1
        vals += v
      }
    }
    val sorted = vals.sorted
    val median = sorted(sorted.length / 2)
    var ans = 0
    sorted.foreach { v => ans += math.abs(v - median) / x }
    ans
  }
}
