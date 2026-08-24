// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

object Solution {
  def secondMinimum(n: Int, edges: Array[Array[Int]], time: Int, change: Int): Int = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e => g(e(0)) += e(1); g(e(1)) += e(0) }
    val dist1 = Array.fill(n + 1)(-1)
    val dist2 = Array.fill(n + 1)(-1)
    val q = scala.collection.mutable.Queue((1, 0))
    dist1(1) = 0
    while (q.nonEmpty) {
      val (u, d) = q.dequeue()
      g(u).foreach { v =>
        val nd = d + 1
        if (dist1(v) == -1) { dist1(v) = nd; q.enqueue((v, nd)) }
        else if (dist2(v) == -1 && nd > dist1(v)) { dist2(v) = nd; q.enqueue((v, nd)) }
      }
    }
    val steps = dist2(n)
    var ans = 0
    var i = 0
    while (i < steps) {
      if ((ans / change) % 2 == 1) ans += change - ans % change
      ans += time
      i += 1
    }
    ans
  }
}
