// LeetCode 3679 - Minimum Discards to Balance Inventory
// https://leetcode.com/problems/minimum-discards-to-balance-inventory/

object Solution {
  def minArrivalsToDiscard(arrivals: Array[Int], w: Int, m: Int): Int = {
    val cnt = new java.util.HashMap[Integer, Integer]()
    val n = arrivals.length
    val marked = new Array[Int](n)
    var ans = 0
    var i = 0
    while (i < n) {
      val x = arrivals(i)
      if (i >= w) cnt.merge(arrivals(i - w), -marked(i - w), Integer.sum)
      if (cnt.getOrDefault(x, 0) >= m) ans += 1
      else {
        marked(i) = 1
        cnt.merge(x, 1, Integer.sum)
      }
      i += 1
    }
    ans
  }
}
