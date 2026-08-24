// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

object Solution {
  def minCost(n: Int, cost: Array[Array[Int]]): Long = {
    val inf = 1L << 60
    val m = n / 2
    val dp = Array.ofDim[Long](3, 3)
    var a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        dp(a)(b) = if (a == b) inf else cost(0)(a).toLong + cost(n - 1)(b)
        b += 1
      }
      a += 1
    }
    var i = 1
    while (i < m) {
      val ndp = Array.fill(3, 3)(inf)
      var pa = 0
      while (pa < 3) {
        var pb = 0
        while (pb < 3) {
          if (dp(pa)(pb) < inf) {
            a = 0
            while (a < 3) {
              if (a != pa) {
                var b = 0
                while (b < 3) {
                  if (!(b == pb || a == b)) {
                    val v = dp(pa)(pb) + cost(i)(a) + cost(n - 1 - i)(b)
                    if (v < ndp(a)(b)) ndp(a)(b) = v
                  }
                  b += 1
                }
              }
              a += 1
            }
          }
          pb += 1
        }
        pa += 1
      }
      a = 0
      while (a < 3) {
        var b = 0
        while (b < 3) {
          dp(a)(b) = ndp(a)(b)
          b += 1
        }
        a += 1
      }
      i += 1
    }
    var ans = inf
    a = 0
    while (a < 3) {
      var b = 0
      while (b < 3) {
        if (dp(a)(b) < ans) ans = dp(a)(b)
        b += 1
      }
      a += 1
    }
    ans
  }
}
