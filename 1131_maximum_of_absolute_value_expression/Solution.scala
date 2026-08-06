// LeetCode 1131 - Maximum of Absolute Value Expression
// https://leetcode.com/problems/maximum-of-absolute-value-expression/

object Solution {
  def maxAbsValExpr(arr1: Array[Int], arr2: Array[Int]): Int = {
    val n = arr1.length
    var ans = 0
    for ((s1, s2) <- Seq((1, 1), (1, -1), (-1, 1), (-1, -1))) {
      var maxv = Int.MinValue
      var minv = Int.MaxValue
      for (i <- 0 until n) {
        val v = s1 * arr1(i) + s2 * arr2(i) + i
        maxv = math.max(maxv, v)
        minv = math.min(minv, v)
      }
      ans = math.max(ans, maxv - minv)
    }
    ans
  }
}
