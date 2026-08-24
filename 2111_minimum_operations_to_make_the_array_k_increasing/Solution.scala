// LeetCode 2111 - Minimum Operations to Make the Array K-Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/

object Solution {
  def kIncreasing(arr: Array[Int], k: Int): Int = {
    var ans = 0
    val n = arr.length
    var start = 0
    while (start < k) {
      val seq = scala.collection.mutable.ArrayBuffer.empty[Int]
      var i = start
      while (i < n) {
        seq += arr(i)
        i += k
      }
      val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
      seq.foreach { x =>
        var lo = 0
        var hi = tails.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (tails(mid) <= x) lo = mid + 1
          else hi = mid
        }
        if (lo == tails.length) tails += x
        else tails(lo) = x
      }
      ans += seq.length - tails.length
      start += 1
    }
    ans
  }
}
