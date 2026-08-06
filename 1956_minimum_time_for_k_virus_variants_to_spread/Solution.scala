// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

object Solution {
  def minDayskVariants(points: Array[Array[Int]], k: Int): Int = {
    var ans = Int.MaxValue
    for (x <- 1 to 100; y <- 1 to 100) {
      val dists = points.map(p => math.abs(p(0) - x) + math.abs(p(1) - y)).sorted
      ans = math.min(ans, dists(k - 1))
    }
    ans
  }
}
