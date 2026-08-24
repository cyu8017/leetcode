// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

object Solution {
  def rotate(grid: Array[Array[Int]]): Array[Array[Int]] = {
    val m = grid.length
    val n = grid(0).length
    val t = Array.ofDim[Int](n, m)
    var i = 0
    while (i < m) {
      var j = 0
      while (j < n) { t(j)(i) = grid(i)(j); j += 1 }
      i += 1
    }
    t
  }

  def check(g: Array[Array[Int]]): Boolean = {
    val m = g.length
    val n = g(0).length
    var s1 = 0L
    var s2 = 0L
    val cnt1 = scala.collection.mutable.HashMap.empty[Long, Int]
    val cnt2 = scala.collection.mutable.HashMap.empty[Long, Int]
    for (row <- g; x <- row) {
      val v = x.toLong
      s2 += v
      cnt2(v) = cnt2.getOrElse(v, 0) + 1
    }
    var i = 0
    while (i < m - 1) {
      for (x <- g(i)) {
        val v = x.toLong
        s1 += v; s2 -= v
        cnt1(v) = cnt1.getOrElse(v, 0) + 1
        cnt2(v) = cnt2(v) - 1
      }
      if (s1 == s2) return true
      if (s1 < s2) {
        val diff = s2 - s1
        if (cnt2.getOrElse(diff, 0) > 0) {
          if ((m - i - 1 > 1 && n > 1) ||
              (i == m - 2 && (g(i + 1)(0) == diff || g(i + 1)(n - 1) == diff)) ||
              (n == 1 && (g(i + 1)(0) == diff || g(m - 1)(0) == diff)))
            return true
        }
      } else {
        val diff = s1 - s2
        if (cnt1.getOrElse(diff, 0) > 0) {
          if ((i + 1 > 1 && n > 1) ||
              (i == 0 && (g(0)(0) == diff || g(0)(n - 1) == diff)) ||
              (n == 1 && (g(0)(0) == diff || g(i)(0) == diff)))
            return true
        }
      }
      i += 1
    }
    false
  }

  def canPartitionGrid(grid: Array[Array[Int]]): Boolean =
    check(grid) || check(rotate(grid))
}
