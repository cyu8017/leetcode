// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

object Solution {
  val INF = 1000000000000000000L

  def minTravelTime(l: Int, n: Int, k: Int, position: Array[Int], time: Array[Int]): Int = {
    val prefix = new Array[Int](n)
    prefix(0) = time(0)
    var i = 1
    while (i < n) { prefix(i) = prefix(i - 1) + time(i); i += 1 }
    val memo = scala.collection.mutable.HashMap.empty[String, Long]

    def dp(i: Int, skips: Int, last: Int): Long = {
      if (i == n - 1) return if (skips == 0) 0L else INF
      val key = i + "," + skips + "," + last
      if (memo.contains(key)) return memo(key)
      var rate = prefix(i)
      if (last > 0) rate -= prefix(last - 1)
      var res = INF
      var end = n - 1
      if (i + skips + 1 < end) end = i + skips + 1
      var j = i + 1
      while (j <= end) {
        val cand = 1L * (position(j) - position(i)) * rate + dp(j, skips - (j - i - 1), i + 1)
        if (cand < res) res = cand
        j += 1
      }
      memo(key) = res
      res
    }

    dp(0, k, 0).toInt
  }
}
