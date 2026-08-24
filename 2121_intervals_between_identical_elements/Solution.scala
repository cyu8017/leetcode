// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

object Solution {
  def getDistances(arr: Array[Int]): Array[Long] = {
    val n = arr.length
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < n) {
      pos.getOrElseUpdate(arr(i), scala.collection.mutable.ArrayBuffer.empty[Int]) += i
      i += 1
    }
    val ans = Array.fill(n)(0L)
    pos.values.foreach { idxs =>
      val m = idxs.length
      val pref = Array.fill(m + 1)(0L)
      i = 0
      while (i < m) {
        pref(i + 1) = pref(i) + idxs(i)
        i += 1
      }
      i = 0
      while (i < m) {
        val left = 1L * i * idxs(i) - pref(i)
        val right = (pref(m) - pref(i + 1)) - 1L * (m - i - 1) * idxs(i)
        ans(idxs(i)) = left + right
        i += 1
      }
    }
    ans
  }
}
