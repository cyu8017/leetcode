// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

object Solution {
  private def opsToZero(x0: Int): Int = {
    var x = x0
    var ops = 0
    while (x > 0) { x /= 4; ops += 1 }
    ops
  }

  def minOperations(queries: Array[Array[Int]]): Long = {
    var ans = 0L
    queries.foreach { q =>
      val l = q(0)
      val r = q(1)
      var sum = 0L
      var x = l
      while (x <= r) {
        sum += opsToZero(x)
        x += 1
      }
      ans += (sum + 1) / 2
    }
    ans
  }
}
