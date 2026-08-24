// LeetCode 3244 - Shortest Distance After Road Addition Queries II
// https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/

object Solution {
  def shortestDistanceAfterQueries(n: Int, queries: Array[Array[Int]]): Array[Int] = {
    val nxt = new Array[Int](n - 1)
    var i = 0
    while (i < n - 1) { nxt(i) = i + 1; i += 1 }
    var cnt = n - 1
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    for (q <- queries) {
      val u = q(0)
      val v = q(1)
      if (nxt(u) > 0 && nxt(u) < v) {
        var cur = nxt(u)
        while (cur < v) {
          cnt -= 1
          val ni = nxt(cur)
          nxt(cur) = 0
          cur = ni
        }
        nxt(u) = v
      }
      ans += cnt
    }
    ans.toArray
  }
}
