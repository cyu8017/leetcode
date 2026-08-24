// LeetCode 0875 - Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/

object Solution {
  def minEatingSpeed(piles: Array[Int], h: Int): Int = {
    var lo = 1
    var hi = piles.max
    while (lo < hi) {
      val mid = (lo + hi) / 2
      var hours = 0L
      piles.foreach { p => hours += (p + mid - 1) / mid }
      if (hours <= h) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
