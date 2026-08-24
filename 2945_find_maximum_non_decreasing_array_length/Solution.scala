// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

object Solution {
  def findMaximumLength(nums: Array[Int]): Int = {
    val n = nums.length
    val pref = Array.ofDim[Long](n + 1)
    val last = Array.ofDim[Long](n + 1)
    var i = 0
    while (i < n) { pref(i + 1) = pref(i) + nums(i); i += 1 }
    val dp = Array.ofDim[Int](n + 1)
    val dq = scala.collection.mutable.ArrayBuffer[Array[Long]](Array(0L, 0L))
    i = 1
    while (i <= n) {
      while (dq.length > 1 && dq(1)(1) <= pref(i)) dq.remove(0)
      val j = dq(0)(0).toInt
      dp(i) = dp(j) + 1
      last(i) = pref(i) - pref(j)
      val value = pref(i) + last(i)
      while (dq.nonEmpty && dq.last(1) >= value) dq.remove(dq.length - 1)
      dq += Array(i.toLong, value)
      i += 1
    }
    dp(n)
  }
}
