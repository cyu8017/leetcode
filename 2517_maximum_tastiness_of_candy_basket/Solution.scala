// LeetCode 2517 - Maximum Tastiness of Candy Basket
// https://leetcode.com/problems/maximum-tastiness-of-candy-basket/

object Solution {
  def maximumTastiness(price: Array[Int], k: Int): Int = {
    scala.util.Sorting.quickSort(price)
    def ok(d: Int): Boolean = {
      var cnt = 1
      var last = price(0)
      var i = 1
      while (i < price.length) {
        if (price(i) - last >= d) {
          cnt += 1
          last = price(i)
          if (cnt >= k) return true
        }
        i += 1
      }
      false
    }
    var lo = 0
    var hi = price(price.length - 1) - price(0)
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid)) lo = mid else hi = mid - 1
    }
    lo
  }
}
