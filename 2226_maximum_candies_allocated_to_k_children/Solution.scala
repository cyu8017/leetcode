// LeetCode 2226 - Maximum Candies Allocated to K Children
// https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

object Solution {
  def maximumCandies(candies: Array[Int], k: Long): Int = {
    def can(mid: Int): Boolean = {
      if (mid == 0) return true
      var cnt = 0L
      for (c <- candies) {
        cnt += c / mid
        if (cnt >= k) return true
      }
      false
    }
    var mx = 0
    for (c <- candies) mx = math.max(mx, c)
    var lo = 0
    var hi = mx
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (can(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
