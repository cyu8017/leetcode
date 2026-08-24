// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

object Solution {
  def maxPartitionFactor(points: Array[Array[Int]]): Int = {
    val n = points.length
    if (n == 2) return 0

    def dist(i: Int, j: Int): Int =
      math.abs(points(i)(0) - points(j)(0)) + math.abs(points(i)(1) - points(j)(1))

    def ok(d: Int): Boolean = {
      val g = Array.fill(n)(new java.util.ArrayList[Integer]())
      var i = 0
      while (i < n) {
        var j = i + 1
        while (j < n) {
          if (dist(i, j) < d) {
            g(i).add(j)
            g(j).add(i)
          }
          j += 1
        }
        i += 1
      }
      val color = Array.fill(n)(-1)
      i = 0
      while (i < n) {
        if (color(i) == -1) {
          val q = new java.util.ArrayDeque[Integer]()
          q.offer(i)
          color(i) = 0
          while (!q.isEmpty) {
            val u = q.poll()
            val it = g(u).iterator()
            while (it.hasNext) {
              val v = it.next().intValue()
              if (color(v) == -1) {
                color(v) = color(u) ^ 1
                q.offer(v)
              } else if (color(v) == color(u)) return false
            }
          }
        }
        i += 1
      }
      true
    }

    var lo = 0
    var hi = 0
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        hi = math.max(hi, dist(i, j))
        j += 1
      }
      i += 1
    }
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
