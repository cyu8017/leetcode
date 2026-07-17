// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

object Solution {
  def countBalls(lowLimit: Int, highLimit: Int): Int = {
    val counts = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    for (value <- lowLimit to highLimit) {
      var box = 0
      var v = value
      while (v > 0) {
        box += v % 10
        v /= 10
      }
      counts(box) += 1
    }
    counts.values.max
  }
}
