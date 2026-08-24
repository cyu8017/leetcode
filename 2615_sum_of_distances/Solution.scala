// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

object Solution {
  def distance(nums: Array[Int]): Array[Long] = {
    val n = nums.length
    val ans = Array.fill(n)(0L)
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    var i = 0
    while (i < n) {
      pos.getOrElseUpdate(nums(i), scala.collection.mutable.ArrayBuffer.empty[Int]) += i
      i += 1
    }
    pos.values.foreach { idxs =>
      val m = idxs.length
      val pref = Array.fill(m + 1)(0L)
      i = 0
      while (i < m) {
        pref(i + 1) = pref(i) + idxs(i)
        i += 1
      }
      var j = 0
      while (j < m) {
        val idx = idxs(j)
        val left = j.toLong * idx - pref(j)
        val right = pref(m) - pref(j + 1) - (m - 1 - j).toLong * idx
        ans(idx) = left + right
        j += 1
      }
    }
    ans
  }
}
