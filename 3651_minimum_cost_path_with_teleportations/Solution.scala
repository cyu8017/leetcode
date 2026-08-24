// LeetCode 3651 - Minimum Cost Path with Teleportations
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/

object Solution {
  def minCost(grid: Array[Array[Int]], k: Int): Int = {
    val m = grid.length
    val n = grid(0).length
    val inf = Int.MaxValue / 4
    val f = Array.ofDim[Int](k + 1, m, n)
    var t = 0
    while (t <= k) {
      var i = 0
      while (i < m) {
        java.util.Arrays.fill(f(t)(i), inf)
        i += 1
      }
      t += 1
    }
    f(0)(0)(0) = 0
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        if (i > 0) f(0)(i)(j) = math.min(f(0)(i)(j), f(0)(i - 1)(j) + grid(i)(j))
        if (j > 0) f(0)(i)(j) = math.min(f(0)(i)(j), f(0)(i)(j - 1) + grid(i)(j))
        j += 1
      }
      i += 1
    }
    val g = new java.util.TreeMap[Integer, java.util.List[Array[Int]]]((a: Integer, b: Integer) => Integer.compare(b, a))
    i = 0
    while (i < m) {
      var j = 0
      while (j < n) {
        g.computeIfAbsent(grid(i)(j), _ => new java.util.ArrayList[Array[Int]]()).add(Array(i, j))
        j += 1
      }
      i += 1
    }
    t = 1
    while (t <= k) {
      var mn = inf
      val vit = g.values().iterator()
      while (vit.hasNext) {
        val pos = vit.next()
        val pit = pos.iterator()
        while (pit.hasNext) {
          val p = pit.next()
          mn = math.min(mn, f(t - 1)(p(0))(p(1)))
        }
        val pit2 = pos.iterator()
        while (pit2.hasNext) {
          val p = pit2.next()
          f(t)(p(0))(p(1)) = mn
        }
      }
      i = 0
      while (i < m) {
        var j = 0
        while (j < n) {
          if (i > 0) f(t)(i)(j) = math.min(f(t)(i)(j), f(t)(i - 1)(j) + grid(i)(j))
          if (j > 0) f(t)(i)(j) = math.min(f(t)(i)(j), f(t)(i)(j - 1) + grid(i)(j))
          j += 1
        }
        i += 1
      }
      t += 1
    }
    var ans = inf
    t = 0
    while (t <= k) {
      ans = math.min(ans, f(t)(m - 1)(n - 1))
      t += 1
    }
    ans
  }
}
