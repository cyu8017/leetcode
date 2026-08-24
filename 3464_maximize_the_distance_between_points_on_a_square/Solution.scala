// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

object Solution {
  private def canPlace(arr: Array[Int], perim: Int, k: Int, mid: Int): Boolean = {
    val n = arr.length
    var s = 0
    while (s < n) {
      var cnt = 1
      var last = arr(s)
      var idx = s
      var stop = false
      while (cnt < k && !stop) {
        val target = last + mid
        var found = false
        var step = 1
        while (step < n && !found) {
          val ni = (idx + step) % n
          val `val` = arr(ni)
          val add = if (ni <= idx) perim else 0
          if (`val` + add >= target) {
            last = `val` + add
            idx = ni
            cnt += 1
            found = true
          }
          step += 1
        }
        if (!found) stop = true
      }
      if (cnt == k && last - arr(s) <= perim - mid) return true
      s += 1
    }
    false
  }

  def maxDistance(side: Int, points: Array[Array[Int]], k: Int): Int = {
    val arr = new Array[Int](points.length)
    var i = 0
    while (i < points.length) {
      val x = points(i)(0)
      val y = points(i)(1)
      val d =
        if (y == 0) x
        else if (x == side) side + y
        else if (y == side) 2 * side + (side - x)
        else 3 * side + (side - y)
      arr(i) = d
      i += 1
    }
    java.util.Arrays.sort(arr)
    val perim = 4 * side
    var lo = 0
    var hi = 2 * side
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (canPlace(arr, perim, k, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
