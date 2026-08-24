// LeetCode 2064 - Minimized Maximum of Products Distributed to Any Store
// https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

object Solution {
  def minimizedMaximum(n: Int, quantities: Array[Int]): Int = {
    def can(x: Int): Boolean = {
      var need = 0
      quantities.foreach { q =>
        need += (q + x - 1) / x
        if (need > n) return false
      }
      true
    }
    var lo = 1
    var hi = 0
    quantities.foreach { q => hi = math.max(hi, q) }
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (can(mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
