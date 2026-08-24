// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

object Solution {
  def countPairs(coordinates: Array[Array[Int]], k: Int): Int = {
    val freq = scala.collection.mutable.Map.empty[Long, Int]
    var ans = 0
    coordinates.foreach { p =>
      val x = p(0)
      val y = p(1)
      for (a <- 0 to k) {
        val b = k - a
        ans += freq.getOrElse(key(x ^ a, y ^ b), 0)
      }
      val kk = key(x, y)
      freq(kk) = freq.getOrElse(kk, 0) + 1
    }
    ans
  }

  private def key(x: Int, y: Int): Long =
    (x.toLong << 32) ^ (y.toLong & 0xffffffffL)
}
