// LeetCode 0441 - Arranging Coins
// https://leetcode.com/problems/arranging-coins/

object Solution {
  def arrangeCoins(n: Int): Int = {
    var low = 0
    var high = n
    while (low <= high) {
      val mid = low + (high - low) / 2
      if (mid.toLong * (mid + 1) / 2 <= n) {
        low = mid + 1
      } else {
        high = mid - 1
      }
    }
    high
  }
}
