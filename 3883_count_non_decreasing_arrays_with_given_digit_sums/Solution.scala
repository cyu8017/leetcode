// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

object Solution {
  def countNonDecreasingArrays(digitSum: Array[Int]): Int = {
    val mod = 1000000007
    val groups = Array.fill(51)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var x = 0
    while (x <= 5000) {
      var s = 0
      var y = x
      while (y > 0) { s += y % 10; y /= 10 }
      groups(s) += x
      x += 1
    }
    var prevVals = groups(digitSum(0))
    var dp = Array.fill(prevVals.length)(1)
    var pos = 1
    while (pos < digitSum.length) {
      val curVals = groups(digitSum(pos))
      val next = new Array[Int](curVals.length)
      var j = 0
      var prefix = 0
      var i = 0
      while (i < curVals.length) {
        val xv = curVals(i)
        while (j < prevVals.length && prevVals(j) <= xv) {
          prefix += dp(j)
          if (prefix >= mod) prefix -= mod
          j += 1
        }
        next(i) = prefix
        i += 1
      }
      prevVals = curVals
      dp = next
      pos += 1
    }
    var ans = 0
    dp.foreach { v =>
      ans += v
      if (ans >= mod) ans -= mod
    }
    ans
  }
}
