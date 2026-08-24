// LeetCode 3639 - Minimum Time to Activate String
// https://leetcode.com/problems/minimum-time-to-activate-string/

object Solution {
  def minTime(s: String, order: Array[Int], k: Int): Int = {
    val n = s.length
    val total = 1L * n * (n + 1) / 2
    if (k > total) return -1

    def countValid(t: Int): Long = {
      val star = Array.fill(n)(false)
      var i = 0
      while (i <= t) {
        star(order(i)) = true
        i += 1
      }
      var invalid = 0L
      i = 0
      while (i < n) {
        if (star(i)) i += 1
        else {
          var j = i
          while (j < n && !star(j)) j += 1
          val L = (j - i).toLong
          invalid += L * (L + 1) / 2
          i = j
        }
      }
      total - invalid
    }

    var lo = 0
    var hi = n - 1
    var ans = -1
    while (lo <= hi) {
      val mid = (lo + hi) / 2
      if (countValid(mid) >= k) {
        ans = mid
        hi = mid - 1
      } else lo = mid + 1
    }
    ans
  }
}
