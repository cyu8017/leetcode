// LeetCode 2187 - Minimum Time to Complete Trips
// https://leetcode.com/problems/minimum-time-to-complete-trips/

object Solution {
  def minimumTime(time: Array[Int], totalTrips: Int): Long = {
    var mn = time(0)
    time.foreach(t => mn = math.min(mn, t))
    var lo = 1L
    var hi = 1L * mn * totalTrips
    while (lo < hi) {
      val mid = (lo + hi) / 2
      var trips = 0L
      var ok = false
      var i = 0
      while (i < time.length && !ok) {
        trips += mid / time(i)
        if (trips >= totalTrips) ok = true
        i += 1
      }
      if (ok) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
