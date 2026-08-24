// LeetCode 0849 - Maximize Distance to Closest Person
// https://leetcode.com/problems/maximize-distance-to-closest-person/

object Solution {
  def maxDistToClosest(seats: Array[Int]): Int = {
    val n = seats.length
    var prev = -1
    var ans = 0
    var i = 0
    while (i < n) {
      if (seats(i) == 1) {
        if (prev == -1) ans = i
        else ans = math.max(ans, (i - prev) / 2)
        prev = i
      }
      i += 1
    }
    math.max(ans, n - 1 - prev)
  }
}
