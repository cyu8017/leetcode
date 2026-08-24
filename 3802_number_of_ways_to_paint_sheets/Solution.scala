// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number-of-ways-to-paint-sheets/

object Solution {
  def numberOfWays(n: Int, limit: Array[Int]): Int = {
    val MOD = 1000000007L
    java.util.Arrays.sort(limit)
    val points = new java.util.ArrayList[Integer]()
    points.add(1)
    points.add(n)
    limit.foreach { x =>
      if (x + 1 > 1 && x + 1 < n) points.add(x + 1)
      if (n - x > 1 && n - x < n) points.add(n - x)
    }
    java.util.Collections.sort(points)
    var u = 0
    var i = 0
    while (i < points.size()) {
      if (u == 0 || !points.get(i).equals(points.get(u - 1))) {
        points.set(u, points.get(i))
        u += 1
      }
      i += 1
    }
    val pts = points.subList(0, u)
    var ans = 0L
    i = 0
    while (i + 1 < pts.size()) {
      val x = pts.get(i)
      val a = countGE(limit, x)
      val b = countGE(limit, n - x)
      val same = countGE(limit, math.max(x, n - x))
      val ways = (a * b - same) % MOD
      val length = pts.get(i + 1).toLong - x
      ans = (ans + ways * length) % MOD
      i += 1
    }
    if (ans < 0) ans += MOD
    ans.toInt
  }

  private def countGE(limit: Array[Int], x: Int): Long = {
    var lo = 0
    var hi = limit.length
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (limit(mid) < x) lo = mid + 1
      else hi = mid
    }
    limit.length - lo
  }
}
