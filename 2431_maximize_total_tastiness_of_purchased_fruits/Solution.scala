// LeetCode 2431 - Maximize Total Tastiness of Purchased Fruits
// https://leetcode.com/problems/maximize-total-tastiness-of-purchased-fruits/

object Solution {
  def maxTastiness(price: Array[Int], tastiness: Array[Int], maxAmount: Int, maxCoupons: Int): Int = {
    val n = price.length
    val dp = Array.fill(maxAmount + 1, maxCoupons + 1)(Int.MinValue / 2)
    dp(0)(0) = 0
    var i = 0
    while (i < n) {
      val p = price(i)
      val t = tastiness(i)
      var a = maxAmount
      while (a >= 0) {
        var c = maxCoupons
        while (c >= 0) {
          if (dp(a)(c) >= 0) {
            if (a + p <= maxAmount) {
              val v = dp(a)(c) + t
              if (v > dp(a + p)(c)) dp(a + p)(c) = v
            }
            if (c + 1 <= maxCoupons && a + p / 2 <= maxAmount) {
              val v = dp(a)(c) + t
              if (v > dp(a + p / 2)(c + 1)) dp(a + p / 2)(c + 1) = v
            }
          }
          c -= 1
        }
        a -= 1
      }
      i += 1
    }
    var ans = 0
    var a2 = 0
    while (a2 <= maxAmount) {
      var c2 = 0
      while (c2 <= maxCoupons) {
        if (dp(a2)(c2) > ans) ans = dp(a2)(c2)
        c2 += 1
      }
      a2 += 1
    }
    ans
  }
}
