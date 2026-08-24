// LeetCode 2594 - Minimum Time to Repair Cars
// https://leetcode.com/problems/minimum-time-to-repair-cars/

object Solution {
  def repairCars(ranks: Array[Int], cars: Int): Long = {
    var mn = Int.MaxValue
    ranks.foreach(r => if (r < mn) mn = r)
    var lo = 1L
    var hi = mn.toLong * cars * cars
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(ranks, cars, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(ranks: Array[Int], cars: Int, t: Long): Boolean = {
    var done = 0L
    ranks.foreach { r =>
      var lo = 0L
      var hi = cars.toLong
      while (lo < hi) {
        val mid = (lo + hi + 1) / 2
        if (r.toLong * mid * mid <= t) lo = mid
        else hi = mid - 1
      }
      done += lo
      if (done >= cars) return true
    }
    done >= cars
  }
}
