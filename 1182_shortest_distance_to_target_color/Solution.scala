// LeetCode 1182 - Shortest Distance to Target Color
// https://leetcode.com/problems/shortest-distance-to-target-color/

object Solution {
  def shortestDistanceColor(colors: Array[Int], queries: Array[Array[Int]]): Array[Int] = {
    val pos = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    for (i <- colors.indices) {
      pos.getOrElseUpdate(colors(i), scala.collection.mutable.ArrayBuffer.empty) += i
    }
    queries.map { q =>
      val i = q(0)
      val c = q(1)
      if (!pos.contains(c)) -1
      else {
        val arr = pos(c)
        var lo = 0
        var hi = arr.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (arr(mid) < i) lo = mid + 1 else hi = mid
        }
        var best = Int.MaxValue
        if (lo < arr.length) best = math.min(best, arr(lo) - i)
        if (lo > 0) best = math.min(best, i - arr(lo - 1))
        if (best == Int.MaxValue) -1 else best
      }
    }
  }
}
