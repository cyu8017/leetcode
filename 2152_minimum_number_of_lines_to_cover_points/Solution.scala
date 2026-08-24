// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

object Solution {
  private def colinear(a: Array[Int], b: Array[Int], c: Array[Int]): Boolean = {
    (b(0) - a(0)) * (c(1) - a(1)) == (c(0) - a(0)) * (b(1) - a(1))
  }

  def minimumLines(points: Array[Array[Int]]): Int = {
    val n = points.length
    if (n <= 2) return 1
    val inf = n
    val dp = Array.fill(1 << n)(inf)
    dp(0) = 0
    var mask = 0
    while (mask < (1 << n)) {
      if (dp(mask) != inf) {
        var i = 0
        while (i < n && (mask & (1 << i)) != 0) i += 1
        if (i < n) {
          var nm = mask | (1 << i)
          dp(nm) = math.min(dp(nm), dp(mask) + 1)
          var j = i + 1
          while (j < n) {
            if ((mask & (1 << j)) == 0) {
              nm = mask | (1 << i) | (1 << j)
              var k = 0
              while (k < n) {
                if ((nm & (1 << k)) == 0 && colinear(points(i), points(j), points(k)))
                  nm |= 1 << k
                k += 1
              }
              dp(nm) = math.min(dp(nm), dp(mask) + 1)
            }
            j += 1
          }
        }
      }
      mask += 1
    }
    dp((1 << n) - 1)
  }
}
