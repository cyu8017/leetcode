// LeetCode 2607 - Make K-Subarray Sums Equal
// https://leetcode.com/problems/make-k-subarray-sums-equal/

object Solution {
  def makeSubKSumEqual(arr: Array[Int], k: Int): Long = {
    val n = arr.length
    val g = gcd(n, k)
    var ans = 0L
    var r = 0
    while (r < g) {
      val group = scala.collection.mutable.ArrayBuffer.empty[Int]
      var i = r
      while (i < n) {
        group += arr(i)
        i += g
      }
      val sorted = group.sorted
      val med = sorted(sorted.length / 2)
      sorted.foreach(x => ans += math.abs(x - med))
      r += 1
    }
    ans
  }

  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }
}
